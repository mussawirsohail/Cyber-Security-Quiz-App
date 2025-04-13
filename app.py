import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(
    page_title="Cybersecurity Fundamentals Quiz",
    page_icon="🔒",
    layout="wide"
)

# Initialize session state variables if they don't exist
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False
if 'questions_shuffled' not in st.session_state:
    st.session_state.questions_shuffled = False
if 'questions' not in st.session_state:
    st.session_state.questions = []

# Define the MCQ data
def load_questions():
    questions = [
        # Week 1
        {
            "week": 1,
            "topic": "Cybersecurity Basics",
            "question": "What does the term 'Cyber' refer to in cybersecurity?",
            "options": [
                "Physical Security",
                "Financial Data",
                "Technology including systems, networks, and data",
                "Antivirus software"
            ],
            "correct_answer": 2,  # 0-indexed, so 2 corresponds to option C
            "explanation": "Cyber refers to technology including systems, networks, and data."
        },
        {
            "week": 1,
            "topic": "Cybersecurity Basics",
            "question": "Which of the following best defines Cybersecurity?",
            "options": [
                "Blocking access to websites",
                "Applying tech and processes to protect systems and data",
                "Installing antivirus only",
                "Monitoring social media"
            ],
            "correct_answer": 1,
            "explanation": "Cybersecurity involves applying technology and processes to protect systems and data."
        },
        {
            "week": 1,
            "topic": "Scope and Need of Cybersecurity",
            "question": "Which of these is not part of the scope of cybersecurity?",
            "options": [
                "Internet of Things (IoT) Security",
                "Cloud Security",
                "Social Media Security",
                "Road Traffic Security"
            ],
            "correct_answer": 3,
            "explanation": "Road Traffic Security is not typically considered part of cybersecurity's scope."
        },
        {
            "week": 1,
            "topic": "Scope and Need of Cybersecurity",
            "question": "One key reason for needing cybersecurity is:",
            "options": [
                "Increasing website views",
                "Safeguarding personal information",
                "Installing paid software",
                "Creating games"
            ],
            "correct_answer": 1,
            "explanation": "Safeguarding personal information is a key reason for cybersecurity."
        },
        {
            "week": 1,
            "topic": "CIA Triad",
            "question": "Which of the following is NOT part of the CIA Triad?",
            "options": [
                "Confidentiality",
                "Integrity",
                "Authentication",
                "Availability"
            ],
            "correct_answer": 2,
            "explanation": "The CIA Triad consists of Confidentiality, Integrity, and Availability. Authentication is not part of it."
        },
        {
            "week": 1,
            "topic": "CIA Triad",
            "question": "Confidentiality in the CIA Triad means:",
            "options": [
                "Hiding data forever",
                "Only authorized people can access the data",
                "Modifying data freely",
                "Data available anytime"
            ],
            "correct_answer": 1,
            "explanation": "Confidentiality ensures that only authorized people can access the data."
        },
        {
            "week": 1,
            "topic": "Threats and Security Breaches",
            "question": "Stuxnet is an example of:",
            "options": [
                "Antivirus",
                "Firewall",
                "Computer worm used in cyber attack",
                "Security patch"
            ],
            "correct_answer": 2,
            "explanation": "Stuxnet was a sophisticated computer worm used in a cyber attack."
        },
        {
            "week": 1,
            "topic": "Threats and Security Breaches",
            "question": "Which of these is a major cause of compromised security?",
            "options": [
                "Daily backups",
                "Lost/stolen devices",
                "Cloud computing",
                "Using HTTPS"
            ],
            "correct_answer": 1,
            "explanation": "Lost or stolen devices are a major cause of security compromises."
        },
        {
            "week": 1,
            "topic": "Cybersecurity Roles",
            "question": "Who tests systems for vulnerabilities by simulating attacks?",
            "options": [
                "Security Consultant",
                "Penetration Tester (Ethical Hacker)",
                "Security Engineer",
                "Threat Intelligence Analyst"
            ],
            "correct_answer": 1,
            "explanation": "Penetration Testers (Ethical Hackers) test systems by simulating attacks."
        },
        {
            "week": 1,
            "topic": "Cybersecurity Roles",
            "question": "The main job of a Security Architect is to:",
            "options": [
                "Train employees",
                "Design secure systems and mitigate threats",
                "Write content",
                "Fix printers"
            ],
            "correct_answer": 1,
            "explanation": "Security Architects design secure systems and develop strategies to mitigate threats."
        },
        {
            "week": 1,
            "topic": "Cybersecurity Teams",
            "question": "Which team simulates attacks to test an organization's defense?",
            "options": [
                "Blue Team",
                "Red Team",
                "Purple Team",
                "Black Hat Team"
            ],
            "correct_answer": 1,
            "explanation": "Red Teams simulate attacks to test an organization's defenses."
        },
        {
            "week": 1,
            "topic": "Cybersecurity Teams",
            "question": "What is the role of a Purple Team?",
            "options": [
                "Conduct only phishing tests",
                "Balance and collaborate Red and Blue Teams",
                "Work for the government only",
                "Write policies"
            ],
            "correct_answer": 1,
            "explanation": "Purple Teams balance and facilitate collaboration between Red and Blue Teams."
        },
        {
            "week": 1,
            "topic": "Professional Development",
            "question": "LinkedIn is important for cybersecurity professionals because:",
            "options": [
                "It lets you download movies",
                "Helps in job search and professional networking",
                "Offers free firewalls",
                "Tracks viruses"
            ],
            "correct_answer": 1,
            "explanation": "LinkedIn helps cybersecurity professionals with job searches and professional networking."
        },
        
        # Week 2
        {
            "week": 2,
            "topic": "Security Operations Center (SOC)",
            "question": "What is the main function of a Security Operations Center (SOC)?",
            "options": [
                "Develop mobile apps",
                "Design websites",
                "Monitor and respond to cyber threats",
                "Manage employee attendance"
            ],
            "correct_answer": 2,
            "explanation": "A SOC's main function is to monitor and respond to cyber threats."
        },
        {
            "week": 2,
            "topic": "Security Operations Center (SOC)",
            "question": "Which technology is central to SOC operations?",
            "options": [
                "QR Code Generator",
                "SIEM (Security Information and Event Management)",
                "Excel",
                "CRM tools"
            ],
            "correct_answer": 1,
            "explanation": "SIEM (Security Information and Event Management) is central to SOC operations."
        },
        {
            "week": 2,
            "topic": "Security Operations Center (SOC)",
            "question": "What is NOT a benefit of a SOC?",
            "options": [
                "Reduced cybersecurity cost",
                "Better collaboration",
                "Developing new operating systems",
                "24/7 monitoring"
            ],
            "correct_answer": 2,
            "explanation": "Developing new operating systems is not a benefit of a SOC."
        },
        {
            "week": 2,
            "topic": "SOC Team Structure",
            "question": "Who leads the SOC team?",
            "options": [
                "Security Intern",
                "SOC Manager/Director",
                "Data Analyst",
                "Marketing Manager"
            ],
            "correct_answer": 1,
            "explanation": "The SOC Manager/Director leads the SOC team."
        },
        {
            "week": 2,
            "topic": "SOC Team Structure",
            "question": "Which of the following is a Level-1 SOC role?",
            "options": [
                "Security Architect",
                "Security Analyst",
                "Penetration Tester",
                "CEO"
            ],
            "correct_answer": 1,
            "explanation": "Security Analyst is typically a Level-1 SOC role."
        },
        {
            "week": 2,
            "topic": "SOC Tools & Technologies",
            "question": "What does an EDR (Endpoint Detection & Response) tool do?",
            "options": [
                "Designs databases",
                "Detects and responds to threats on endpoints",
                "Schedules meetings",
                "Sends newsletters"
            ],
            "correct_answer": 1,
            "explanation": "EDR tools detect and respond to threats on endpoints (like computers and mobile devices)."
        },
        {
            "week": 2,
            "topic": "SOC Tools & Technologies",
            "question": "What is the purpose of UEBA tools?",
            "options": [
                "Manage HR data",
                "Monitor behavior patterns to detect threats",
                "Backup media files",
                "Track sales leads"
            ],
            "correct_answer": 1,
            "explanation": "UEBA (User and Entity Behavior Analytics) tools monitor behavior patterns to detect threats."
        },
        {
            "week": 2,
            "topic": "Penetration Testing",
            "question": "Penetration Testing is also known as:",
            "options": [
                "White Hat Coding",
                "Ethical Hacking",
                "Malware Deployment",
                "Software Engineering"
            ],
            "correct_answer": 1,
            "explanation": "Penetration Testing is also known as Ethical Hacking."
        },
        {
            "week": 2,
            "topic": "Penetration Testing",
            "question": "Which of the following best describes a SOC Analyst?",
            "options": [
                "Red Team Member",
                "Offensive Role",
                "Blue Team Member",
                "Graphic Designer"
            ],
            "correct_answer": 2,
            "explanation": "A SOC Analyst is typically considered a Blue Team Member (defensive role)."
        },
        {
            "week": 2,
            "topic": "Security Controls",
            "question": "Which of the following is an Administrative Control?",
            "options": [
                "Antivirus Software",
                "Employee Training Programs",
                "Firewalls",
                "Surveillance Cameras"
            ],
            "correct_answer": 1,
            "explanation": "Employee Training Programs are an example of Administrative Controls."
        },
        {
            "week": 2,
            "topic": "Security Controls",
            "question": "Firewalls and Encryption fall under which control type?",
            "options": [
                "Physical",
                "Administrative",
                "Technical",
                "Procedural"
            ],
            "correct_answer": 2,
            "explanation": "Firewalls and Encryption are examples of Technical Controls."
        },
        {
            "week": 2,
            "topic": "Security Controls",
            "question": "Fingerprint scanners and locks are part of:",
            "options": [
                "Technical Controls",
                "Administrative Controls",
                "Physical Controls",
                "Digital Controls"
            ],
            "correct_answer": 2,
            "explanation": "Fingerprint scanners and locks are examples of Physical Controls."
        },
        {
            "week": 2,
            "topic": "Identity, Authentication & Authorization",
            "question": "Authentication means:",
            "options": [
                "Giving access to files",
                "Verifying someone's identity",
                "Installing new software",
                "Encrypting data"
            ],
            "correct_answer": 1,
            "explanation": "Authentication is the process of verifying someone's identity."
        },
        {
            "week": 2,
            "topic": "Identity, Authentication & Authorization",
            "question": "Which of the following is an example of Property-based authentication?",
            "options": [
                "Password",
                "Fingerprint",
                "Access Card",
                "Facial Expression"
            ],
            "correct_answer": 2,
            "explanation": "An Access Card is an example of Property-based authentication (something you have)."
        },
        {
            "week": 2,
            "topic": "Identity, Authentication & Authorization",
            "question": "Multifactor Authentication uses:",
            "options": [
                "Only passwords",
                "Two or more types of authentication",
                "Same password twice",
                "Single sign-on only"
            ],
            "correct_answer": 1,
            "explanation": "Multifactor Authentication uses two or more types of authentication factors."
        },
        {
            "week": 2,
            "topic": "Identity, Authentication & Authorization",
            "question": "Authorization helps ensure:",
            "options": [
                "System updates",
                "Limited and secure access",
                "UI improvements",
                "Device charging"
            ],
            "correct_answer": 1,
            "explanation": "Authorization helps ensure limited and secure access to resources."
        },
        
        # Week 3
        {
            "week": 3,
            "topic": "Non-Repudiation & Risk Basics",
            "question": "What does Non-Repudiation ensure?",
            "options": [
                "Quick response time",
                "Easy password reset",
                "Proof of origin and data integrity",
                "Fast logins"
            ],
            "correct_answer": 2,
            "explanation": "Non-Repudiation ensures proof of origin and data integrity, preventing denial of actions."
        },
        {
            "week": 3,
            "topic": "Non-Repudiation & Risk Basics",
            "question": "Which of the following best defines a vulnerability?",
            "options": [
                "The act of hacking",
                "Flaw in a system that can be exploited",
                "Antivirus software",
                "A firewall feature"
            ],
            "correct_answer": 1,
            "explanation": "A vulnerability is a flaw in a system that can be exploited."
        },
        {
            "week": 3,
            "topic": "Non-Repudiation & Risk Basics",
            "question": "A threat is:",
            "options": [
                "A security camera",
                "A user's login",
                "A potential for exploiting a vulnerability",
                "Data backup"
            ],
            "correct_answer": 2,
            "explanation": "A threat is a potential for exploiting a vulnerability."
        },
        {
            "week": 3,
            "topic": "Non-Repudiation & Risk Basics",
            "question": "What is a risk in cybersecurity?",
            "options": [
                "Cost of installing software",
                "Probability of loss due to a threat exploiting a vulnerability",
                "Number of passwords used",
                "Random software crash"
            ],
            "correct_answer": 1,
            "explanation": "Risk is the probability of loss due to a threat exploiting a vulnerability."
        },
        {
            "week": 3,
            "topic": "Social Engineering Attacks",
            "question": "Social Engineering attacks primarily rely on:",
            "options": [
                "Malware",
                "Password cracking",
                "Psychological manipulation",
                "Network scanning"
            ],
            "correct_answer": 2,
            "explanation": "Social Engineering attacks primarily rely on psychological manipulation."
        },
        {
            "week": 3,
            "topic": "Social Engineering Attacks",
            "question": "Which of these is an example of Social Engineering?",
            "options": [
                "Firewall misconfiguration",
                "Phishing email asking for login details",
                "Network packet loss",
                "USB encryption"
            ],
            "correct_answer": 1,
            "explanation": "A phishing email asking for login details is an example of Social Engineering."
        },
        {
            "week": 3,
            "topic": "Social Engineering Attacks",
            "question": "Pretexting involves:",
            "options": [
                "Sending viruses",
                "Using false stories to get sensitive info",
                "Encrypting files",
                "Denial of service"
            ],
            "correct_answer": 1,
            "explanation": "Pretexting involves using false stories to get sensitive information."
        },
        {
            "week": 3,
            "topic": "Types of Phishing",
            "question": "Which phishing type targets specific individuals or companies?",
            "options": [
                "Email Phishing",
                "Vishing",
                "Spear Phishing",
                "Clone Phishing"
            ],
            "correct_answer": 2,
            "explanation": "Spear Phishing targets specific individuals or companies."
        },
        {
            "week": 3,
            "topic": "Types of Phishing",
            "question": "Which of the following is NOT a phishing method?",
            "options": [
                "Baiting",
                "HTTPS Phishing",
                "Pop-up Phishing",
                "Angler Phishing"
            ],
            "correct_answer": 0,
            "explanation": "Baiting is a social engineering technique but not specifically a phishing method."
        },
        {
            "week": 3,
            "topic": "Malware & Ransomware",
            "question": "What is a Trojan?",
            "options": [
                "A self-replicating malware",
                "A malware that pretends to be legit software",
                "Antivirus software",
                "System update tool"
            ],
            "correct_answer": 1,
            "explanation": "A Trojan is malware that pretends to be legitimate software."
        },
        {
            "week": 3,
            "topic": "Malware & Ransomware",
            "question": "Which malware allows remote control and disables antivirus?",
            "options": [
                "Adware",
                "Spyware",
                "Rootkits",
                "Worms"
            ],
            "correct_answer": 2,
            "explanation": "Rootkits allow remote control and often disable antivirus software."
        },
        {
            "week": 3,
            "topic": "Malware & Ransomware",
            "question": "Ransomware typically:",
            "options": [
                "Makes apps crash",
                "Encrypts data and demands money",
                "Slows down browsing",
                "Deletes backups only"
            ],
            "correct_answer": 1,
            "explanation": "Ransomware typically encrypts data and demands money for decryption."
        },
        {
            "week": 3,
            "topic": "Passwords & MFA",
            "question": "What is the purpose of Username and Password Authentication?",
            "options": [
                "Grant system admin access",
                "Log IP addresses",
                "Verify user identity",
                "Scan for viruses"
            ],
            "correct_answer": 2,
            "explanation": "Username and Password Authentication is used to verify user identity."
        },
        {
            "week": 3,
            "topic": "Passwords & MFA",
            "question": "Which of the following is NOT a factor in Multi-Factor Authentication (MFA)?",
            "options": [
                "Something you know",
                "Something you have",
                "Something you guess",
                "Something you are"
            ],
            "correct_answer": 2,
            "explanation": "The three factors in MFA are something you know, have, and are. 'Something you guess' is not a factor."
        },
        {
            "week": 3,
            "topic": "Passwords & MFA",
            "question": "What does the 'Inherence Factor' refer to in MFA?",
            "options": [
                "Your device",
                "Your password",
                "Your fingerprint or biometrics",
                "Your home address"
            ],
            "correct_answer": 2,
            "explanation": "The 'Inherence Factor' refers to biometrics - something you are (fingerprint, face, etc.)."
        },
        
        # Week 4
        {
            "week": 4,
            "topic": "Risk Management",
            "question": "Risk is best defined as:",
            "options": [
                "A weakness in a system",
                "The potential for loss when a threat exploits a vulnerability",
                "A natural disaster",
                "The cost of cybersecurity tools"
            ],
            "correct_answer": 1,
            "explanation": "Risk combines the likelihood of a threat exploiting a vulnerability and its consequences."
        },
        {
            "week": 4,
            "topic": "Risk Management",
            "question": "Which stage of risk management involves analyzing the impact of identified risks?",
            "options": [
                "Identify",
                "Assess",
                "Control",
                "Review"
            ],
            "correct_answer": 1,
            "explanation": "The 'Assess' stage evaluates the likelihood and impact of risks."
        },
        {
            "week": 4,
            "topic": "Risk Management",
            "question": "Which of the following is NOT a vulnerability?",
            "options": [
                "Software bugs",
                "Hackers",
                "Legacy systems",
                "Human error"
            ],
            "correct_answer": 1,
            "explanation": "Hackers are threats, not vulnerabilities."
        },
        {
            "week": 4,
            "topic": "Business Continuity",
            "question": "ISO 22301 is primarily associated with:",
            "options": [
                "Disaster Recovery",
                "Business Continuity Management",
                "Load Balancing",
                "Risk Identification"
            ],
            "correct_answer": 1,
            "explanation": "ISO 22301 is the international standard for Business Continuity Management Systems (BCMS)."
        },
        {
            "week": 4,
            "topic": "Disaster Recovery",
            "question": "The 'Response' phase in Disaster Recovery includes:",
            "options": [
                "Conducting drills",
                "Implementing disaster response plans",
                "Buying insurance policies",
                "Rebuilding structures"
            ],
            "correct_answer": 1,
            "explanation": "The Response phase occurs during/immediately after a disaster (e.g., activating plans)."
        },
        {
            "week": 4,
            "topic": "Business Continuity",
            "question": "Which component is part of a Business Continuity Plan (BCP)?",
            "options": [
                "Load balancing",
                "Roles & Responsibilities",
                "Multi-factor authentication",
                "Data replication"
            ],
            "correct_answer": 1,
            "explanation": "Roles & Responsibilities ensure clarity during disruptions."
        },
        {
            "week": 4,
            "topic": "High Availability",
            "question": "High Availability (HA) ensures:",
            "options": [
                "Equal traffic distribution",
                "Continuous operation without downtime",
                "Compliance with ISO 27001",
                "Reduced insurance costs"
            ],
            "correct_answer": 1,
            "explanation": "HA focuses on maintaining uptime through redundancy."
        },
        {
            "week": 4,
            "topic": "Load Balancing",
            "question": "Load Balancing improves:",
            "options": [
                "Regulatory compliance",
                "Network traffic distribution",
                "Employee training",
                "Risk assessment accuracy"
            ],
            "correct_answer": 1,
            "explanation": "Load balancing distributes traffic across resources to optimize performance."
        },
        {
            "week": 4,
            "topic": "Disaster Types",
            "question": "Which is a man-made disaster?",
            "options": [
                "Flood",
                "Earthquake",
                "Cyber attack",
                "Volcanic eruption"
            ],
            "correct_answer": 2,
            "explanation": "Cyber attacks are intentional, human-caused disruptions."
        },
        {
            "week": 4,
            "topic": "Disaster Recovery",
            "question": "The 'Mitigation' phase in Disaster Recovery includes:",
            "options": [
                "Creating evacuation plans",
                "Digging water channels to prevent flooding",
                "Testing backup systems",
                "Restoring data"
            ],
            "correct_answer": 1,
            "explanation": "Mitigation involves actions to reduce disaster impact (e.g., infrastructure changes)."
        },
        {
            "week": 4,
            "topic": "Disaster Recovery",
            "question": "Which is NOT a benefit of a Disaster Recovery Plan?",
            "options": [
                "Faster recovery",
                "Reduced compliance",
                "Enhanced security",
                "Cost savings"
            ],
            "correct_answer": 1,
            "explanation": "DR plans improve compliance, not reduce it."
        },
        {
            "week": 4,
            "topic": "Risk Components",
            "question": "Which term describes weaknesses that threats exploit?",
            "options": [
                "Consequences",
                "Vulnerabilities",
                "Risks",
                "Controls"
            ],
            "correct_answer": 1,
            "explanation": "Vulnerabilities are weaknesses in systems or processes."
        },
        {
            "week": 4,
            "topic": "Risk Components",
            "question": "Which is a 'Threat'?",
            "options": [
                "Broken processes",
                "Criminals",
                "Financial loss",
                "Data backup"
            ],
            "correct_answer": 1,
            "explanation": "Criminals are external threats that can cause harm."
        },
        {
            "week": 4,
            "topic": "Risk Management",
            "question": "The final stage of Risk Management is:",
            "options": [
                "Identify",
                "Assess",
                "Control",
                "Review"
            ],
            "correct_answer": 3,
            "explanation": "The four stages are Identify > Assess > Control > Review."
        },
        {
            "week": 4,
            "topic": "Disaster Recovery",
            "question": "Which activity falls under 'Preparedness' in Disaster Recovery?",
            "options": [
                "Conducting search and rescue",
                "Developing supply lists",
                "Rebuilding structures",
                "Updating software"
            ],
            "correct_answer": 1,
            "explanation": "Preparedness involves planning and readiness activities like creating supply lists."
        },
        {
            "week": 4,
            "topic": "High Availability",
            "question": "High Availability (HA) is most critical for:",
            "options": [
                "Reducing insurance costs",
                "Ensuring 24/7 system uptime",
                "Distributing network traffic",
                "Training employees"
            ],
            "correct_answer": 1,
            "explanation": "HA minimizes downtime through failover mechanisms."
        },
        {
            "week": 4,
            "topic": "Business Continuity",
            "question": "Which is a key component of ISO 22301?",
            "options": [
                "Data encryption",
                "Continuous improvement",
                "Load balancing",
                "Threat hunting"
            ],
            "correct_answer": 1,
            "explanation": "ISO 22301 emphasizes regular audits and continuous improvement of BCMS."
        },
        {
            "week": 4,
            "topic": "Disaster Recovery",
            "question": "Which phase ensures systems operate normally after a disaster?",
            "options": [
                "Prevention",
                "Response",
                "Recovery",
                "Mitigation"
            ],
            "correct_answer": 2,
            "explanation": "Recovery focuses on restoring operations post-disaster."
        },
        {
            "week": 4,
            "topic": "Access Management",
            "question": "Privileged Access Management (PAM) is a:",
            "options": [
                "Risk assessment tool",
                "Risk control method",
                "Disaster Recovery phase",
                "Load balancing technique"
            ],
            "correct_answer": 1,
            "explanation": "PAM is a control to mitigate risks by managing access."
        },
        {
            "week": 4,
            "topic": "Load Balancing",
            "question": "Which is a benefit of Load Balancing?",
            "options": [
                "Legal penalties reduction",
                "Improved user experience",
                "Business impact analysis",
                "Threat identification"
            ],
            "correct_answer": 1,
            "explanation": "Load balancing improves performance, enhancing user experience."
        },
        
        # Week 5
        {
            "week": 5,
            "topic": "Defense in Depth",
            "question": "Defense in Depth (DiD) primarily focuses on:",
            "options": [
                "Using a single firewall for all protection",
                "Layering security controls across multiple levels",
                "Reducing employee training costs",
                "Eliminating physical security measures"
            ],
            "correct_answer": 1,
            "explanation": "DiD uses multiple layers (network, host, application, data) to create a resilient security posture."
        },
        {
            "week": 5,
            "topic": "Defense in Depth",
            "question": "Which layer of Defense in Depth protects against internal workstation threats?",
            "options": [
                "Perimeter Defense",
                "Host Protection",
                "Data Encryption",
                "Application Server Security"
            ],
            "correct_answer": 1,
            "explanation": "Host Protection secures workstations from both internal and external attacks."
        },
        {
            "week": 5,
            "topic": "Separation of Duties",
            "question": "Separation of Duties (SoD) is designed to mitigate:",
            "options": [
                "Natural disasters",
                "Insider threats and fraud",
                "Network latency",
                "Data encryption failures"
            ],
            "correct_answer": 1,
            "explanation": "SoD prevents errors/fraud by dividing tasks among multiple users."
        },
        {
            "week": 5,
            "topic": "Separation of Duties",
            "question": "Which scenario violates Separation of Duties?",
            "options": [
                "Person A writes a PO, Person B approves it",
                "Person C approves invoices and signs checks",
                "Person D monitors audit trails",
                "Person E encrypts sensitive data"
            ],
            "correct_answer": 1,
            "explanation": "Combining invoice approval and check signing creates a conflict of interest."
        },
        {
            "week": 5,
            "topic": "Privileged Access Management",
            "question": "Privileged Access Management (PAM) is used to:",
            "options": [
                "Distribute network traffic",
                "Monitor and restrict elevated user access",
                "Encrypt all employee emails",
                "Automate disaster recovery"
            ],
            "correct_answer": 1,
            "explanation": "PAM controls and monitors privileged accounts (e.g., admin, superuser)."
        },
        {
            "week": 5,
            "topic": "Privileged Access Management",
            "question": "Which is a feature of PAM?",
            "options": [
                "Load balancing",
                "Password vaults",
                "Risk assessment templates",
                "Firewall configurations"
            ],
            "correct_answer": 1,
            "explanation": "Password vaults securely store credentials, a key PAM feature."
        },
        {
            "week": 5,
            "topic": "Access Control Models",
            "question": "MAC (Mandatory Access Control) is commonly used in:",
            "options": [
                "Small startups",
                "Government/military environments",
                "Retail businesses",
                "Educational institutions"
            ],
            "correct_answer": 1,
            "explanation": "MAC enforces strict, administrator-defined access rules, typical in high-security settings."
        },
        {
            "week": 5,
            "topic": "Access Control Models",
            "question": "DAC (Discretionary Access Control) allows:",
            "options": [
                "Administrators to set all permissions",
                "Users to transfer ownership of data",
                "Rules based on time of access",
                "Automatic role-based permissions"
            ],
            "correct_answer": 1,
            "explanation": "DAC lets owners grant/restrict access using ACLs."
        },
        {
            "week": 5,
            "topic": "Access Control Models",
            "question": "RBAC (Role-Based Access Control) assigns permissions based on:",
            "options": [
                "User attributes like location",
                "Predefined rules",
                "Job roles within an organization",
                "Encryption standards"
            ],
            "correct_answer": 2,
            "explanation": "RBAC groups permissions by roles (e.g., 'Manager,' 'Developer')."
        },
        {
            "week": 5,
            "topic": "Access Control Models",
            "question": "ABAC (Attribute-Based Access Control) evaluates:",
            "options": [
                "Only user roles",
                "Environmental factors like time and location",
                "Physical security layers",
                "Compliance penalties"
            ],
            "correct_answer": 1,
            "explanation": "ABAC uses attributes (e.g., time, clearance level) for granular access control."
        },
        {
            "week": 5,
            "topic": "Access Control Models",
            "question": "Which access control model uses predefined rules regardless of user roles?",
            "options": [
                "MAC",
                "RBAC",
                "RuBAC",
                "DAC"
            ],
            "correct_answer": 2,
            "explanation": "Rule-Based Access Control (RuBAC) relies on fixed rules set by administrators."
        },
        {
            "week": 5,
            "topic": "Emergency Access",
            "question": "A 'Break the Glass' account is associated with:",
            "options": [
                "Disaster Recovery",
                "Emergency privileged access",
                "Load balancing",
                "ISO 22301 compliance"
            ],
            "correct_answer": 1,
            "explanation": "Emergency accounts allow access during critical system failures."
        },
        {
            "week": 5,
            "topic": "Privileged Access Management",
            "question": "Which is NOT a benefit of PAM?",
            "options": [
                "Preventing credential sharing",
                "Reducing compliance costs",
                "Real-time monitoring of risky behavior",
                "Integrating with SIEM tools"
            ],
            "correct_answer": 1,
            "explanation": "PAM ensures compliance but does not inherently reduce compliance costs."
        },
        {
            "week": 5,
            "topic": "Separation of Duties",
            "question": "The 'four eyes principle' in SoD ensures:",
            "options": [
                "Two people review critical actions",
                "Four layers of network defense",
                "Quarterly audits",
                "Automated backups"
            ],
            "correct_answer": 0,
            "explanation": "The principle requires dual approval for sensitive tasks to prevent errors/fraud."
        },
        {
            "week": 5,
            "topic": "Separation of Duties",
            "question": "Which is a risk of Separation of Duties?",
            "options": [
                "Improved efficiency",
                "Increased collusion potential",
                "Simplified workflows",
                "Reduced compliance"
            ],
            "correct_answer": 1,
            "explanation": "SoD can lead to collusion if multiple users conspire to bypass controls."
        }
    ]
    return questions

# Function to shuffle questions
def shuffle_questions():
    questions = load_questions()
    random.shuffle(questions)
    st.session_state.questions = questions
    st.session_state.questions_shuffled = True

# Function to handle next question
def next_question():
    # Save the current answer if selected
    if st.session_state.selected_option is not None:
        st.session_state.answers[st.session_state.current_question] = st.session_state.selected_option
    
    # Move to next question
    st.session_state.current_question += 1
    st.session_state.selected_option = None

# Function to handle previous question
def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1
        # Restore previous answer if it exists
        if st.session_state.current_question in st.session_state.answers:
            st.session_state.selected_option = st.session_state.answers[st.session_state.current_question]
        else:
            st.session_state.selected_option = None

# Function to finish quiz
def finish_quiz():
    # Save the last answer if selected
    if st.session_state.selected_option is not None:
        st.session_state.answers[st.session_state.current_question] = st.session_state.selected_option
    
    st.session_state.quiz_complete = True

# Function to restart quiz
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_complete = False
    st.session_state.selected_option = None
    st.session_state.questions_shuffled = False

# Initialize selected_option if it doesn't exist
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

# Main app
def main():
    st.title("🔒 Cybersecurity Fundamentals Quiz")
    
    # Shuffle questions if not already done
    if not st.session_state.questions_shuffled:
        shuffle_questions()
    
    # If quiz is complete, show results
    if st.session_state.quiz_complete:
        show_results()
    else:
        # Show quiz
        show_quiz()

def show_quiz():
    questions = st.session_state.questions
    current_q_idx = st.session_state.current_question
    
    # Check if we've reached the end of questions
    if current_q_idx >= len(questions):
        st.warning("You've reached the end of the questions. Please finish the quiz to see your results.")
        if st.button("Finish Quiz", key="finish_end"):
            st.session_state.quiz_complete = True
            st.rerun()
        return
    
    current_q = questions[current_q_idx]
    
    # Progress bar
    progress = (current_q_idx) / len(questions)
    st.progress(progress)
    st.write(f"Question {current_q_idx + 1} of {len(questions)}")
    
    # Display week and topic
    st.markdown(f"**Week {current_q.get('week')}**: {current_q.get('topic')}")
    
    # Display question
    st.markdown(f"### {current_q.get('question')}")
    
    # Radio buttons for options
    option_labels = ["A", "B", "C", "D"]
    options = current_q.get('options')
    
    # Create radio buttons with the actual options - FIX: Make sure we don't go out of bounds
    option_items = []
    for i, option in enumerate(options):
        if i < len(option_labels):  # Only add options that have corresponding labels
            option_items.append(f"{option_labels[i]}: {option}")
    
    selected_option = st.radio(
        "Select your answer:",
        option_items,
        index=None if st.session_state.selected_option is None else st.session_state.selected_option,
        key=f"radio_{current_q_idx}"
    )
    
    # Update selected_option based on radio selection
    if selected_option:
        # Extract the index from the selected option
        selected_index = option_labels.index(selected_option.split(":")[0])
        st.session_state.selected_option = selected_index
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if current_q_idx > 0:
            if st.button("Previous", key="prev"):
                prev_question()
                st.rerun()
    
    with col2:
        if st.button("Next", key="next"):
            next_question()
            st.rerun()
    
    with col3:
        if st.button("Finish Quiz", key="finish"):
            finish_quiz()
            st.rerun()

def show_results():
    st.header("Quiz Results")
    
    questions = st.session_state.questions
    answers = st.session_state.answers
    
    # Calculate score
    correct_count = 0
    for q_idx, user_answer in answers.items():
        if q_idx < len(questions):  # Safety check
            correct_answer = questions[q_idx].get('correct_answer')
            if user_answer == correct_answer:
                correct_count += 1
    
    total_questions = len(answers)
    if total_questions > 0:
        score_percentage = (correct_count / total_questions) * 100
    else:
        score_percentage = 0
    
    # Display score
    st.markdown(f"### Your Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")
    
    # Score interpretation
    if score_percentage >= 90:
        st.success("🌟 Excellent! You have a strong understanding of cybersecurity fundamentals!")
    elif score_percentage >= 75:
        st.success("👍 Good job! You have a solid grasp of the material.")
    elif score_percentage >= 60:
        st.warning("🔍 You're on the right track, but might need to review some concepts.")
    else:
        st.error("📚 You should spend more time studying the material.")
    
    # Show detailed results
    st.markdown("### Detailed Results")
    
    # Create a DataFrame for better visualization
    results_data = []
    for q_idx, user_answer in answers.items():
        if q_idx < len(questions):  # Safety check
            q = questions[q_idx]
            correct_answer = q.get('correct_answer')
            is_correct = user_answer == correct_answer
            
            results_data.append({
                "Week": q.get('week'),
                "Topic": q.get('topic'),
                "Question": q.get('question'),
                "Your Answer": f"{chr(65 + user_answer)}: {q.get('options')[user_answer]}",
                "Correct Answer": f"{chr(65 + correct_answer)}: {q.get('options')[correct_answer]}",
                "Result": "✅ Correct" if is_correct else "❌ Incorrect",
                "Explanation": q.get('explanation')
            })
    
    # Convert to DataFrame
    results_df = pd.DataFrame(results_data)
    
    # Display results with expanders for each question
    for i, row in results_df.iterrows():
        with st.expander(f"Question {i+1}: {row['Question']} ({row['Result']})"):
            st.write(f"**Topic:** {row['Topic']} (Week {row['Week']})")
            st.write(f"**Your Answer:** {row['Your Answer']}")
            st.write(f"**Correct Answer:** {row['Correct Answer']}")
            st.write(f"**Explanation:** {row['Explanation']}")
    
    # Option to restart quiz
    if st.button("Restart Quiz"):
        restart_quiz()
        st.rerun()
    
    # Option to download results as CSV
    csv = results_df.to_csv(index=False)
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name="cybersecurity_quiz_results.csv",
        mime="text/csv"
    )

# Run the app
if __name__ == "__main__":
    main()