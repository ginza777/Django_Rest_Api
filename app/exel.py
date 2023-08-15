import xlwt

def export_users_to_excel(users, filename):
    # Create a new workbook and add a sheet
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('User Data')

    # Define header row
    header = [
        'ID', 'Username', 'Email', 'First Name', 'Last Name',
        'Is Active', 'Is Staff', 'Is Superuser', 'Date Joined', 'Phone', 'Privileges'
    ]

    # Write header row
    for col, header_text in enumerate(header):
        sheet.write(0, col, header_text)

    # Write data rows
    for row, user in enumerate(users, start=1):
        sheet.write(row, 0, user.id)
        sheet.write(row, 1, user.username)
        sheet.write(row, 2, user.email)
        sheet.write(row, 3, user.first_name)
        sheet.write(row, 4, user.last_name)
        sheet.write(row, 5, user.is_active)
        sheet.write(row, 6, user.is_staff)
        sheet.write(row, 7, user.is_superuser)
        sheet.write(row, 8, user.date_joined.strftime('%Y-%m-%d %H:%M:%S'))
        sheet.write(row, 9, str(user.phone))
        sheet.write(row, 10, user.privaligies)

    # Save the workbook to the specified filename
    workbook.save(filename)
