import csv
from django.http import HttpResponse


def export_users_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First Name', 'Last Name', 'Email'])

    for user in queryset:
        writer.writerow([user.username, user.first_name, user.last_name, user.email])

    return response
export_users_to_excel.short_description = "Export selected users to Excel"
