-- Normalized Relational Schema for Amazon RDS PostgreSQL
CREATE TABLE usm_institutions (
    institution_id SERIAL PRIMARY KEY,
    institution_name VARCHAR(120) UNIQUE NOT NULL,
    county VARCHAR(60),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    yoy_change_pct DECIMAL(5,2),
    avg_annual_change_pct DECIMAL(5,2)
);

CREATE TABLE transfer_cohorts (
    cohort_id SERIAL PRIMARY KEY,
    institution_id INT REFERENCES usm_institutions(institution_id) ON DELETE CASCADE,
    fiscal_year INT NOT NULL CHECK (fiscal_year BETWEEN 2022 AND 2026),
    transfer_students INT NOT NULL CHECK (transfer_students >= 0),
    UNIQUE (institution_id, fiscal_year)
);

-- Query 1: Total & Average 5-Year Transfer Enrollment by Institution
SELECT 
    i.institution_name,
    SUM(c.transfer_students) AS total_5yr_transfers,
    ROUND(AVG(c.transfer_students), 1) AS avg_annual_transfers,
    i.avg_annual_change_pct
FROM transfer_cohorts c
JOIN usm_institutions i ON c.institution_id = i.institution_id
GROUP BY i.institution_name, i.avg_annual_change_pct
ORDER BY total_5yr_transfers DESC;

-- Query 2: Institutions with Positive Multi-Year Growth
SELECT institution_name, yoy_change_pct, avg_annual_change_pct
FROM usm_institutions
WHERE avg_annual_change_pct > 0
ORDER BY avg_annual_change_pct DESC;