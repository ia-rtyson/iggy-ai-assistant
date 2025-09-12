SELECT
    ica.id,
    ica."timestamp",
    ica.ignition_chat_history_id,
    ica.artifact_type_id,
    at.name AS artifact_type,
    ica.data,
    ica.public,
    ica.final
FROM
    public.ignition_chat_artifacts AS ica
INNER JOIN
    public.artifact_type AS at ON ica.artifact_type_id = at.id
WHERE
    ica.ignition_chat_history_id = :ignition_chat_history_id
ORDER BY
    ica."timestamp" ASC;