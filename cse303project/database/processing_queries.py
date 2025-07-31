
from .user_queries import execute_query
from .connection import DB_TYPE

def add_processing_session(session_name, session_date, notes):
    """Add a new processing session"""
    query = (
        'INSERT INTO processing_sessions (session_name, session_date, notes) VALUES (%s, %s, %s)'
        if DB_TYPE == 'mysql'
        else 'INSERT INTO processing_sessions (session_name, session_date, notes) VALUES (?, ?, ?)'
    )
    params = (session_name, session_date, notes)
    return execute_query(query, params)

def get_all_processing_sessions():
    """Get all processing sessions"""
    return execute_query('SELECT * FROM processing_sessions ORDER BY session_date DESC', fetch_all=True)

def get_processing_session_by_id(session_id):
    """Get a single processing session by ID"""
    query = 'SELECT * FROM processing_sessions WHERE id = %s' if DB_TYPE == 'mysql' else 'SELECT * FROM processing_sessions WHERE id = ?'
    return execute_query(query, (session_id,), fetch_one=True)

def add_processing_input(session_id, batch_id, quantity_used):
    """Add an input batch to a processing session"""
    query = (
        'INSERT INTO processing_inputs (session_id, batch_id, quantity_used) VALUES (%s, %s, %s)'
        if DB_TYPE == 'mysql'
        else 'INSERT INTO processing_inputs (session_id, batch_id, quantity_used) VALUES (?, ?, ?)'
    )
    params = (session_id, batch_id, quantity_used)
    return execute_query(query, params)

def get_processing_inputs_for_session(session_id):
    """Get all input batches for a given processing session"""
    query = '''
        SELECT pi.*, b.batch_number, p.name as product_name
        FROM processing_inputs pi
        JOIN inventory_batches b ON pi.batch_id = b.id
        JOIN products p ON b.product_id = p.id
        WHERE pi.session_id = %s
        ORDER BY pi.id
    ''' if DB_TYPE == 'mysql' else '''
        SELECT pi.*, b.batch_number, p.name as product_name
        FROM processing_inputs pi
        JOIN inventory_batches b ON pi.batch_id = b.id
        JOIN products p ON b.product_id = p.id
        WHERE pi.session_id = ?
        ORDER BY pi.id
    '''
    return execute_query(query, (session_id,), fetch_all=True)

def add_processing_output(session_id, product_id, output_type, weight):
    """Add an output product to a processing session"""
    query = (
        'INSERT INTO processing_outputs (session_id, product_id, output_type, weight) VALUES (%s, %s, %s, %s)'
        if DB_TYPE == 'mysql'
        else 'INSERT INTO processing_outputs (session_id, product_id, output_type, weight) VALUES (?, ?, ?, ?)'
    )
    params = (session_id, product_id, output_type, weight)
    return execute_query(query, params)

def get_processing_outputs_for_session(session_id):
    """Get all output products for a given processing session"""
    query = '''
        SELECT po.*, p.name as product_name
        FROM processing_outputs po
        JOIN products p ON po.product_id = p.id
        WHERE po.session_id = %s
        ORDER BY po.id
    ''' if DB_TYPE == 'mysql' else '''
        SELECT po.*, p.name as product_name
        FROM processing_outputs po
        JOIN products p ON po.product_id = p.id
        WHERE po.session_id = ?
        ORDER BY po.id
    '''
    return execute_query(query, (session_id,), fetch_all=True)
