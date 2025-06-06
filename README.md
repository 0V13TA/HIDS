# Host-Based Intrusion Detection/Prevention System (HIDS/HIPS)

A **Host-Based Intrusion Detection System (HIDS)** is a security solution that monitors and analyzes the internal state of a computing system—such as its operating system, application logs, and file integrity—to detect signs of malicious activity or policy violations. Unlike network-based systems, HIDS operates directly on individual hosts, enabling it to identify unauthorized changes, suspicious processes, or abnormal user behavior. This provides system administrators with detailed insights and timely alerts.

## Key Features of HIDS

- **File Integrity Monitoring:** Detects unauthorized modifications by tracking changes to critical system and application files.
- **Log Analysis:** Reviews system and application logs for suspicious activities or policy breaches.
- **Process Monitoring:** Observes running processes to identify abnormal or unauthorized behavior.
- **User Activity Monitoring:** Tracks user actions to detect privilege escalation or unusual access patterns.
- **Rootkit Detection:** Scans for hidden malware or rootkits that may compromise system integrity.
- **Real-Time Alerts:** Notifies administrators immediately upon detecting suspicious events.
- **Policy Enforcement:** Monitors configuration changes to ensure compliance with security policies.
- **Automated Response:** Executes predefined actions, such as blocking processes or isolating the host, when threats are detected.

## Benefits of HIDS

- **Early Threat Detection:** Identifies malicious activity on individual hosts before it can spread across the network.
- **Detailed Forensics:** Provides granular logs and evidence to support incident investigation and response.
- **Policy Compliance:** Helps meet regulatory and organizational security requirements.
- **Protection for Critical Assets:** Monitors sensitive systems and data that may not be visible to network-based solutions.
- **Customizable Monitoring:** Supports tailored rules and alerts specific to each host’s role and risk profile.
- **Reduced False Positives:** Uses context-aware analysis to distinguish between legitimate and suspicious activities.
- **Supports Incident Response:** Enables rapid containment and remediation of detected threats.

## Project Scope

Due to time constraints, this project will focus solely on file integrity monitoring. The approach involves creating cryptographic hashes for all files within a protected directory and periodically verifying these hashes to detect any unauthorized modifications.

## Technologies Used

- **Python:** Core programming language.
- **PySide6:** For building the graphical user interface (GUI).
- **hashlib:** For generating file hashes.
- **schedule:** For scheduling periodic integrity checks in a cron-like manner.
