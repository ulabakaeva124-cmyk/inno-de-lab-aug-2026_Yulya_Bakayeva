#Task 4
requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]
required_admin_roles = {"admin", "security_officer",
"audit_manager"}
unique_roles = set(requested_roles)
unique_required_roles = unique_roles & required_admin_roles
missing_roles = required_admin_roles - unique_roles
security_officer = "security_officer" in unique_roles

print(f'Уникальные запрошенные роли: {unique_roles}\n'
      f'Общие административные роли: {unique_required_roles}\n'
      f'Недостающие административные роли: {missing_roles}\n'
      f'Наличие роли security_officer в запросе: {security_officer}')