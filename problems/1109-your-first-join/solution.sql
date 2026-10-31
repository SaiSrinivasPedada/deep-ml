-- Employee name + department name
SELECT employees.name, departments.name
FROM departments
INNER JOIN employees ON employees.department_id = departments.id