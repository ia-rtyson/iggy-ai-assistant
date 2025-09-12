UPDATE instructions
SET
    name        = :name,
    description = :description,
    content     = :content
WHERE id = :id;