with renamed as (

    select 
        id as lead_id,
        name as lead_name,
        department as lead_department,
        salary as lead_salary,
        hire_date as lead_hire_date,
        status as lead_status,
        current_timestamp as lead_loaded_at 
    from {{ ref('raw_seed_new_filw') }}

)

select * from renamed