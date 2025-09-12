SELECT
    ica.*,
    at.name AS artifact_type_name
FROM
    ignition_chat_artifacts AS ica
JOIN
    artifact_type AS at ON ica.artifact_type_id = at.id
WHERE
    ica.id = :id;