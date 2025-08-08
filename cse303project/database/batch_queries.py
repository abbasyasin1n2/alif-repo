from .user_queries import execute_query
from .connection import DB_TYPE

def add_batch(product_id, batch_number, quantity, arrival_date, expiration_date, storage_location):
    """Add a new inventory batch"""
    query = (
        'INSERT INTO inventory_batches (product_id, batch_number, quantity, arrival_date, expiration_date, storage_location) VALUES (%s, %s, %s, %s, %s, %s)'
        if DB_TYPE == 'mysql'
        else 'INSERT INTO inventory_batches (product_id, batch_number, quantity, arrival_date, expiration_date, storage_location) VALUES (?, ?, ?, ?, ?, ?)'
    )
    params = (product_id, batch_number, quantity, arrival_date, expiration_date, storage_location)
    return execute_query(query, params)

def get_all_batches():
    """Get all inventory batches with product and storage location information"""
    query = '''
        SELECT b.*, p.name as product_name, sl.name as storage_name, sl.location_type as storage_type
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        LEFT JOIN storage_locations sl ON b.storage_location = sl.id
        ORDER BY b.arrival_date DESC
    '''
    return execute_query(query, fetch_all=True)

def get_batch_by_id(batch_id):
    """Get a single inventory batch by ID with storage information"""
    query = '''
        SELECT b.*, sl.name as storage_name, sl.location_type as storage_type, sl.capacity as storage_capacity
        FROM inventory_batches b
        LEFT JOIN storage_locations sl ON b.storage_location = sl.id
        WHERE b.id = %s
    ''' if DB_TYPE == 'mysql' else '''
        SELECT b.*, sl.name as storage_name, sl.location_type as storage_type, sl.capacity as storage_capacity
        FROM inventory_batches b
        LEFT JOIN storage_locations sl ON b.storage_location = sl.id
        WHERE b.id = ?
    '''
    return execute_query(query, (batch_id,), fetch_one=True)

def update_batch(batch_id, product_id, batch_number, quantity, arrival_date, expiration_date, storage_location):
    """Update an existing inventory batch"""
    query = (
        'UPDATE inventory_batches SET product_id = %s, batch_number = %s, quantity = %s, arrival_date = %s, expiration_date = %s, storage_location = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s'
        if DB_TYPE == 'mysql'
        else 'UPDATE inventory_batches SET product_id = ?, batch_number = ?, quantity = ?, arrival_date = ?, expiration_date = ?, storage_location = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?'
    )
    params = (product_id, batch_number, quantity, arrival_date, expiration_date, storage_location, batch_id)
    return execute_query(query, params)

def update_batch_quantity(batch_id, quantity_change):
    """Update the quantity of an inventory batch"""
    query = (
        'UPDATE inventory_batches SET quantity = quantity - %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s'
        if DB_TYPE == 'mysql'
        else 'UPDATE inventory_batches SET quantity = quantity - ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?'
    )
    params = (quantity_change, batch_id)
    return execute_query(query, params)

def delete_batch(batch_id):
    """Delete an inventory batch"""
    query = 'DELETE FROM inventory_batches WHERE id = %s' if DB_TYPE == 'mysql' else 'DELETE FROM inventory_batches WHERE id = ?'
    return execute_query(query, (batch_id,))

def get_expired_batches():
    """Get all batches that have passed their expiration date"""
    query = """
        SELECT b.*, p.name as product_name
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        WHERE b.expiration_date < CURDATE() AND b.quantity > 0
        ORDER BY b.expiration_date ASC
    """ if DB_TYPE == 'mysql' else """
        SELECT b.*, p.name as product_name
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        WHERE b.expiration_date < DATE('now') AND b.quantity > 0
        ORDER BY b.expiration_date ASC
    """
    return execute_query(query, fetch_all=True)

def get_soon_to_expire_batches(days=7):
    """Get all batches that will expire within a certain number of days"""
    query = """
        SELECT b.*, p.name as product_name
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        WHERE b.expiration_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL %s DAY) AND b.quantity > 0
        ORDER BY b.expiration_date ASC
    """ if DB_TYPE == 'mysql' else """
        SELECT b.*, p.name as product_name
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        WHERE b.expiration_date BETWEEN DATE('now') AND DATE('now', '+{} days') AND b.quantity > 0
        ORDER BY b.expiration_date ASC
    """.format(days)
    params = (days,) if DB_TYPE == 'mysql' else ()
    return execute_query(query, params, fetch_all=True)

def get_inventory_over_time():
    """Get the sum of inventory quantities grouped by arrival date"""
    query = """
        SELECT arrival_date, SUM(quantity) as total_quantity
        FROM inventory_batches
        GROUP BY arrival_date
        ORDER BY arrival_date ASC
    """
    return execute_query(query, fetch_all=True)


def get_batch_compliance_status(batch_id):
    """Get comprehensive compliance status for a batch"""
    from datetime import datetime, timedelta
    
    # Get batch details
    batch = get_batch_by_id(batch_id)
    if not batch:
        return {'status': 'unknown', 'issues': ['Batch not found']}
    
    issues = []
    status = 'normal'
    
    # Check expiration status
    if batch.get('expiration_date'):
        exp_date = batch['expiration_date']
        if isinstance(exp_date, str):
            exp_date = datetime.strptime(exp_date, '%Y-%m-%d').date()
        
        today = datetime.now().date()
        days_to_expire = (exp_date - today).days
        
        if days_to_expire < 0:
            status = 'critical'
            issues.append(f'Expired {abs(days_to_expire)} days ago')
        elif days_to_expire <= 7:
            status = 'warning' if status == 'normal' else status
            issues.append(f'Expires in {days_to_expire} days')
    
    # Check for recalls
    try:
        from database.recall_queries import get_batch_recall_history
        recall_history = get_batch_recall_history(batch_id)
        if recall_history:
            active_recalls = [r for r in recall_history if r.get('status') in ['initiated', 'in_progress']]
            if active_recalls:
                status = 'critical'
                issues.append(f'{len(active_recalls)} active recall(s)')
    except ImportError:
        pass  # Recall functionality not available
    
    # Check storage alerts (if storage location is available)
    if batch.get('storage_location'):
        try:
            from database.storage_queries import get_alert_readings
            alerts = get_alert_readings()
            storage_alerts = [a for a in alerts if str(a.get('storage_id')) == str(batch['storage_location'])]
            if storage_alerts:
                status = 'warning' if status == 'normal' else status
                issues.append(f'{len(storage_alerts)} storage alert(s)')
        except ImportError:
            pass  # Storage functionality not available
    
    return {
        'status': status,
        'issues': issues,
        'batch_id': batch_id
    }
