SELECT person.firstname as first_name,
        person.lastname as last_name,
        employee.vacationhours as pto
FROM person.person
JOIN humanresources.employee 
    ON person.businessentityid = humanresources.employee.businessentityid
WHERE employee.vacationhours  >= 40
GROUP BY person.businessentityid, pto
LIMIT 10; 
