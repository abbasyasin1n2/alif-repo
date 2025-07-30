
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..database import (
    get_all_suppliers, add_supplier, get_supplier_by_id, update_supplier, delete_supplier,
    get_all_products, add_product, get_product_by_id, update_product, delete_product
)

inventory_bp = Blueprint('inventory', __name__, template_folder='templates')

# Supplier Routes
@inventory_bp.route('/suppliers')
@login_required
def list_suppliers():
    suppliers = get_all_suppliers()
    return render_template('inventory/list_suppliers.html', suppliers=suppliers)

@inventory_bp.route('/suppliers/add', methods=['GET', 'POST'])
@login_required
def add_supplier_route():
    if request.method == 'POST':
        name = request.form['name']
        contact_person = request.form['contact_person']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        add_supplier(name, contact_person, phone, email, address)
        flash('Supplier added successfully!', 'success')
        return redirect(url_for('inventory.list_suppliers'))
    return render_template('inventory/add_supplier.html')

@inventory_bp.route('/suppliers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_supplier(id):
    supplier = get_supplier_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        contact_person = request.form['contact_person']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        update_supplier(id, name, contact_person, phone, email, address)
        flash('Supplier updated successfully!', 'success')
        return redirect(url_for('inventory.list_suppliers'))
    return render_template('inventory/edit_supplier.html', supplier=supplier)

@inventory_bp.route('/suppliers/delete/<int:id>', methods=['POST'])
@login_required
def delete_supplier_route(id):
    delete_supplier(id)
    flash('Supplier deleted successfully!', 'success')
    return redirect(url_for('inventory.list_suppliers'))

# Product Routes
@inventory_bp.route('/products')
@login_required
def list_products():
    products = get_all_products()
    return render_template('inventory/list_products.html', products=products)

@inventory_bp.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product_route():
    if request.method == 'POST':
        name = request.form['name']
        animal_type = request.form['animal_type']
        cut_type = request.form['cut_type']
        processing_date = request.form['processing_date']
        storage_requirements = request.form['storage_requirements']
        shelf_life = request.form['shelf_life']
        packaging_details = request.form['packaging_details']
        supplier_id = request.form['supplier_id']
        add_product(name, animal_type, cut_type, processing_date, storage_requirements, shelf_life, packaging_details, supplier_id)
        flash('Product added successfully!', 'success')
        return redirect(url_for('inventory.list_products'))
    
    suppliers = get_all_suppliers()
    return render_template('inventory/add_product.html', suppliers=suppliers)

@inventory_bp.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = get_product_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        animal_type = request.form['animal_type']
        cut_type = request.form['cut_type']
        processing_date = request.form['processing_date']
        storage_requirements = request.form['storage_requirements']
        shelf_life = request.form['shelf_life']
        packaging_details = request.form['packaging_details']
        supplier_id = request.form['supplier_id']
        update_product(id, name, animal_type, cut_type, processing_date, storage_requirements, shelf_life, packaging_details, supplier_id)
        flash('Product updated successfully!', 'success')
        return redirect(url_for('inventory.list_products'))

    suppliers = get_all_suppliers()
    return render_template('inventory/edit_product.html', product=product, suppliers=suppliers)

@inventory_bp.route('/products/delete/<int:id>', methods=['POST'])
@login_required
def delete_product_route(id):
    delete_product(id)
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('inventory.list_products'))
