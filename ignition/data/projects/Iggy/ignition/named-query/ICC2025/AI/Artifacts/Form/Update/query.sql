UPDATE form_configs 
SET name = :name,
    description = :description,
    config_json = :config_json,
    updated_at = CURRENT_TIMESTAMP
WHERE uuid = :uuid;