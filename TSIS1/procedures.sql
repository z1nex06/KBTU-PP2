CREATE OR REPLACE FUNCTION _get_contact_id(p_name TEXT)
RETURNS INT AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid
    FROM contacts
    WHERE (first_name || ' ' || surname) ILIKE p_name
    LIMIT 1;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    RETURN cid;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE add_phone(p_contact_name TEXT, p_phone TEXT, p_type TEXT)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    cid := _get_contact_id(p_contact_name);

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, LOWER(p_type));
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name TEXT, p_group TEXT)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
DECLARE gid INT;
BEGIN
    cid := _get_contact_id(p_contact_name);

    SELECT id INTO gid FROM groups WHERE name ILIKE p_group;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES (p_group) RETURNING id INTO gid;
    END IF;

    UPDATE contacts SET group_id = gid WHERE id = cid;
END;
$$;


CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INT,
    name TEXT,
    email TEXT,
    birthday DATE,
    group_name TEXT,
    phones TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.first_name || ' ' || c.surname,
        c.email,
        c.birthday,
        g.name,
        STRING_AGG(p.phone || '('||p.type||')', ', ')
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE
        c.first_name ILIKE '%'||p_query||'%'
        OR c.surname ILIKE '%'||p_query||'%'
        OR c.email ILIKE '%'||p_query||'%'
        OR p.phone ILIKE '%'||p_query||'%'
    GROUP BY c.id, g.name;
END;
$$;