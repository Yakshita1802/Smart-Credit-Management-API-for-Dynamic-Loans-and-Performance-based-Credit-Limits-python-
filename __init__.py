@credit_management_bp.route('/loans/process', methods=['POST'])
def add_loan_process():
    loan_data = request.get_json()
    borrower_id = loan_data.get('borrowerId')
    loan_amount = loan_data.get('loanAmount')

    # Check if the borrower exists in the loan table
    existing_loan = get_loan_by_id(borrower_id)
    if not existing_loan:
        # If the borrower is new, set their credit limit to 5000
        credit_limit = 5000
    else:
        # Retrieve the borrower's credit limit from the credit limit table
        credit_limit_data = get_credit_limit(borrower_id)
        credit_limit = credit_limit_data.get('creditLimit')

    # Check if there are any existing unpaid loans with crossed repayment dates
    existing_unpaid_loans = get_existing_unpaid_loans(borrower_id)
    if existing_unpaid_loans:
        return jsonify({"message": "Loan application rejected. Unpaid loans exist with crossed repayment dates.", "status": "error"})

    # Check if the loan amount exceeds the remaining credit limit available to the borrower
    remaining_credit_limit = credit_limit - get_used_credit_amount(borrower_id)
    if loan_amount > remaining_credit_limit:
        return jsonify({"message": "Loan application rejected. Loan amount exceeds available credit limit.", "status": "error"})

    # If all checks pass, approve the loan application and update credit limit
    add_loan(loan_data)
    update_credit_limit(borrower_id, loan_amount)

    return jsonify({"message": "Loan application approved and transferred", "status": "success"})
