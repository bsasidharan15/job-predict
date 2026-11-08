-- ============================================
-- JOB ACCEPTANCE PREDICTION - SQL SETUP
-- File: sql_database_setup.sql
-- Database: MySQL
-- ============================================

/* -------------------------------
   1. CREATE DATABASE
--------------------------------*/
CREATE DATABASE IF NOT EXISTS job_acceptance_ml_db;
USE job_acceptance_ml_db;

/* -------------------------------
   2. DROP TABLE (SAFE RESET)
--------------------------------*/
DROP TABLE IF EXISTS job_acceptance_data;

/* -------------------------------
   3. CREATE MAIN TABLE
--------------------------------*/
CREATE TABLE job_acceptance_data (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,

    age_years INT,
    gender VARCHAR(10),

    ssc_percentage DECIMAL(5,2),
    hsc_percentage DECIMAL(5,2),
    degree_percentage DECIMAL(5,2),
    degree_specialization VARCHAR(50),

    technical_score DECIMAL(5,2),
    aptitude_score DECIMAL(5,2),
    communication_score DECIMAL(5,2),

    skills_match_percentage DECIMAL(5,2),
    certifications_count INT,
    internship_experience VARCHAR(10),
    years_of_experience DECIMAL(4,1),

    career_switch_willingness VARCHAR(15),
    relevant_experience VARCHAR(15),

    previous_ctc_lpa DECIMAL(6,2),
    expected_ctc_lpa DECIMAL(6,2),

    company_tier VARCHAR(10),
    job_role_match VARCHAR(15),
    competition_level VARCHAR(15),
    bond_requirement VARCHAR(15),

    notice_period_days INT,
    layoff_history VARCHAR(10),
    employment_gap_months INT,
    relocation_willingness VARCHAR(15),

    placement_status VARCHAR(15),


    placement_probability_score DECIMAL(5,2),
    risk_score DECIMAL(4,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



 

/* -------------------------------
   4. INSERT SAMPLE REALISTIC DATA
   (This is OPTIONAL – testing only)
--------------------------------*/
INSERT INTO job_acceptance_data (
    age_years, gender, ssc_percentage, hsc_percentage, degree_percentage,
    degree_specialization, technical_score, aptitude_score,
    communication_score, skills_match_percentage,
    certifications_count, internship_experience, years_of_experience,
    career_switch_willingness, relevant_experience,
    previous_ctc_lpa, expected_ctc_lpa,
    company_tier, job_role_match, competition_level,
    bond_requirement, notice_period_days,
    layoff_history, employment_gap_months,
    relocation_willingness, placement_status,
    placement_probability_score, risk_score
)
VALUES
(23,'Male',82.5,78.2,75.4,'Computer Science',85,78,72,80,
 2,'Yes',1.5,'Willing','Relevant',
 4.5,7.0,'Tier 1','Matched','Medium',
 'No',30,'No',2,'Willing','Placed',82.3,0.25),

(28,'Female',75.1,72.3,70.8,'Electronics',68,65,70,60,
 1,'No',4.0,'Not Willing','Not Relevant',
 6.0,10.5,'Tier 2','Not Matched','High',
 'Yes',60,'Yes',10,'Not Willing','Not Placed',38.6,0.72);


/* -------------------------------
   5. IMPORTANT ANALYSIS QUERIES
--------------------------------*/

-- Placement rate
SELECT
    status,
    COUNT(*) AS total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_acceptance_data),2) AS percentage
FROM job_acceptance_data
GROUP BY status;

-- High risk candidates
SELECT 
    placement_status,
    COUNT(*) AS total,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_acceptance_data),
        2
    ) AS percentage
FROM job_acceptance_data
GROUP BY placement_status;

-- Avg placement probability by experience
SELECT
    CASE
        WHEN years_of_experience = 0 THEN 'Fresher'
        WHEN years_of_experience BETWEEN 1 AND 3 THEN 'Junior'
        WHEN years_of_experience BETWEEN 4 AND 7 THEN 'Mid'
        ELSE 'Senior'
    END AS experience_level,
    ROUND(AVG(placement_probability_score),2) AS avg_probability
FROM job_acceptance_data
GROUP BY experience_level;

