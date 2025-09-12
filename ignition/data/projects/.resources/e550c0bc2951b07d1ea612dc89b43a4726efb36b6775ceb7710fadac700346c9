SELECT
    item_id,
    "timestamp",
    session_id,
    event_type,
    content
FROM (
    -- First, select all the messages for the specific session
    SELECT
        nch.id AS item_id,
        nch."timestamp",
        nch.session_id,
        'message' AS event_type,
        nch.message::text AS content
    FROM
        public.n8n_chat_history AS nch
    WHERE nch.session_id = :chat_id AND nch.hide IS FALSE

    UNION ALL

    -- Second, select all the artifacts for the specific session
    SELECT
        ica.id AS item_id,
        ica."timestamp",
        ich.chat_id AS session_id,
        at.name AS event_type,
        ica.data AS content
    FROM
        public.ignition_chat_artifacts AS ica
    INNER JOIN
        public.ignition_chat_history AS ich ON ica.ignition_chat_history_id = ich.id
    INNER JOIN
        public.artifact_type AS at ON ica.artifact_type_id = at.id
    WHERE ich.chat_id = :chat_id
) AS chat_feed -- The subquery must have an alias
ORDER BY
    "timestamp" ASC;