#Task 4
requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]
required_admin_roles = {"admin", "security_officer",
"audit_manager"}
unique_roles = {role for role in requested_roles}
unique_required_roles = {role for role in unique_roles if role in required_admin_roles}
missing_roles = {role for role in required_admin_roles if role not in requested_roles}
security_officer = False
if "security_officer" in requested_roles:
    security_officer = True
print(f'Уникальные запрошенные роли: {unique_roles}\n'
      f'Общие административные роли: {required_admin_roles}\n'
      f'Недостающие административные роли: {unique_roles}\n'
      f'Наличие роли security_officer в запросе: {security_officer}')