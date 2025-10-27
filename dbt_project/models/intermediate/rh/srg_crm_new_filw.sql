with department_salary_stats as (
    select 
        lead_department,
        avg(lead_salary) as avg_salary,
        max(lead_salary) as max_salary,
        min(lead_salary) as min_salary
    from 
        {{ ref('stg_crm_new_filw') }}
    group by 
        lead_department
)

select * from department_salary_stats