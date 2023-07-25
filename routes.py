from flask import Blueprint, jsonify
from credit_management.service import add_loan,get_loan_by_id,get_loans_by_borrowers_id,get_all_loans,get_credit_limit,get_paymentdetails,loan_repayment

credit_management_bp = Blueprint('credit_management', __name__)



@credit_management_bp.route('/loans/process', methods=['POST'])
def add_loan_process():
    loans = add_loan()
    return jsonify(loans)


@credit_management_bp.route('/loans/:id', methods=['GET'])
def get_loans_by_id_def(loan_id):
    loans = get_loan_by_id(loan_id)
    return jsonify(loans)

@credit_management_bp.route('/loans/borrowers/:id', methods=['GET'])
def get_loans_by_borrowers_id_def(borrowers_id):
    loans = get_loans_by_borrowers_id(borrowers_id)
    return jsonify(loans)

@credit_management_bp.route('/loans', methods=['GET'])
def get_all_loans_def():
    loans = get_all_loans()
    return jsonify(loans)

@credit_management_bp.route('/loans/creditlimit/:id', methods=['GET'])
def get_credit_limit_def(borrowers_id):
    loans = get_credit_limit(borrowers_id)
    return jsonify(loans)

@credit_management_bp.route('/loans/paymentdetails/:id', methods=['GET'])
def get_paymentdetails_def(loan_id):
    loans = get_paymentdetails(loan_id)
    return jsonify(loans)

@credit_management_bp.route('/loans/paymentdetails/:id/repayment', methods=['POST'])
def loan_repayment_def(loan_id):
    loans = loan_repayment(loan_id)
    return jsonify(loans)
    
    

