
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
    """Get all inventory batches with product information"""
    query = '''
        SELECT b.*, p.name as product_name
        FROM inventory_batches b
        JOIN products p ON b.product_id = p.id
        ORDER BY b.arrival_date DESC
    '''
    return execute_query(query, fetch_all=True)

def get_batch_by_id(batch_id):
    """Get a single inventory batch by ID"""
    query = 'SELECT * FROM inventory_batches WHERE id = %s' if DB_TYPE == 'mysql' else 'SELECT * FROM inventory_batches WHERE id = ?'
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

def delete_batch(batch_id):
    """Delete an inventory batch"""
    query = 'DELETE FROM inventory_batches WHERE id = %s' if DB_TYPE == 'mysql' else 'DELETE FROM inventory_batches WHERE id = ?'
    return execute_query(query, (batch_id,))
