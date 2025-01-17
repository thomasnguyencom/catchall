import csv

# Define the data
roles = [
    ("Role", "Level", "Description", "Compensation"),
    ("Software Engineer", "Junior", "Entry-level developer proficient in a programming language and basic software engineering concepts. Works under close supervision.", "$70k–$90k/year"),
    ("Software Engineer", "Mid-level", "Has 3–5 years of experience, can independently handle assigned modules, and understands design patterns and system architecture basics.", "$90k–$120k/year"),
    ("Software Engineer", "Senior", "Over 5 years of experience, capable of leading projects, mentoring juniors, and designing scalable systems.", "$120k–$160k/year"),
    ("UI/UX Designer", "Junior", "Skilled in basic design tools and creating wireframes. Works under supervision to implement designs.", "$60k–$80k/year"),
    ("UI/UX Designer", "Mid-level", "3–5 years of experience with expertise in design systems and user research. Can own small projects.", "$80k–$100k/year"),
    ("UI/UX Designer", "Senior", "5+ years of experience, leads design strategy, conducts extensive user testing, and mentors others.", "$100k–$130k/year"),
    ("QA Engineer/Tester", "Junior", "Basic knowledge of testing frameworks and tools. Focuses on executing test cases and logging issues.", "$55k–$75k/year"),
    ("QA Engineer/Tester", "Mid-level", "Experienced in writing test scripts and performing automation testing. Works independently.", "$75k–$95k/year"),
    ("QA Engineer/Tester", "Senior", "5+ years of experience, designs test strategies, and integrates testing into CI/CD pipelines.", "$95k–$125k/year"),
    ("DevOps Engineer", "Junior", "Familiar with basic CI/CD pipelines and cloud platforms. Works on predefined tasks.", "$80k–$100k/year"),
    ("DevOps Engineer", "Mid-level", "Experienced with managing infrastructure, scripting, and monitoring tools.", "$100k–$130k/year"),
    ("DevOps Engineer", "Senior", "Leads infrastructure architecture, cost optimization, and team mentoring.", "$130k–$170k/year"),
    ("Product Manager", "Junior", "Assists in backlog grooming and gathering requirements under supervision.", "$70k–$90k/year"),
    ("Product Manager", "Mid-level", "Manages product roadmaps and prioritizes development cycles.", "$90k–$120k/year"),
    ("Product Manager", "Senior", "Drives long-term product strategy and represents the product vision across teams.", "$120k–$150k/year"),
    ("Scrum Master", "Junior", "Supports Agile ceremonies and learns to facilitate team activities.", "$60k–$80k/year"),
    ("Scrum Master", "Mid-level", "Independently leads Agile teams, ensures alignment with Agile principles.", "$80k–$110k/year"),
    ("Scrum Master", "Senior", "Coaches teams across the organization and drives Agile adoption strategies.", "$110k–$140k/year"),
    ("Business Analyst", "Junior", "Gathers requirements and prepares documentation under supervision.", "$60k–$80k/year"),
    ("Business Analyst", "Mid-level", "Experienced in facilitating stakeholder workshops and analyzing complex requirements.", "$80k–$100k/year"),
    ("Business Analyst", "Senior", "Leads enterprise-level requirement analysis and mentors junior analysts.", "$100k–$130k/year"),
    ("Data Engineer", "Junior", "Works on basic data pipelines and understands ETL concepts.", "$70k–$90k/year"),
    ("Data Engineer", "Mid-level", "Builds scalable pipelines and integrates various data sources.", "$90k–$120k/year"),
    ("Data Engineer", "Senior", "Oversees data architecture, governance, and performance optimization.", "$120k–$160k/year"),
    ("System Administrator", "Junior", "Manages basic IT tasks, troubleshooting, and user account setups.", "$50k–$70k/year"),
    ("System Administrator", "Mid-level", "Handles system configurations and infrastructure optimizations.", "$70k–$90k/year"),
    ("System Administrator", "Senior", "Leads IT strategy, implements advanced security measures, and manages cross-system integrations.", "$90k–$120k/year"),
    ("Security Specialist", "Junior", "Assists in vulnerability scans and basic incident response.", "$70k–$90k/year"),
    ("Security Specialist", "Mid-level", "Conducts threat analysis and configures security tools.", "$90k–$120k/year"),
    ("Security Specialist", "Senior", "Develops organization-wide security policies and oversees compliance.", "$120k–$150k/year"),
    ("Change Manager", "Junior", "Supports communication and training for small change initiatives.", "$60k–$80k/year"),
    ("Change Manager", "Mid-level", "Plans and executes change management projects.", "$80k–$110k/year"),
    ("Change Manager", "Senior", "Develops change management frameworks and leads enterprise initiatives.", "$110k–$140k/year"),
    ("Documentation Specialist", "Junior", "Writes basic user manuals and internal documentation.", "$50k–$70k/year"),
    ("Documentation Specialist", "Mid-level", "Creates detailed technical documents and ensures consistency.", "$70k–$90k/year"),
    ("Documentation Specialist", "Senior", "Manages documentation projects and integrates them into development cycles.", "$90k–$110k/year"),
    ("Project Manager", "Junior", "Assists in scheduling, tracking progress, and reporting under the guidance of a senior manager.", "$65k–$85k/year"),
    ("Project Manager", "Mid-level", "Leads project teams, manages budgets, and ensures timely delivery of small to medium projects.", "$85k–$115k/year"),
    ("Project Manager", "Senior", "Drives strategic projects, oversees large cross-functional teams, and manages risks and stakeholder relationships.", "$115k–$150k/year"),
    ("Data Scientist", "Junior", "Supports data analysis and visualization tasks, works under senior guidance.", "$80k–$100k/year"),
    ("Data Scientist", "Mid-level", "Develops predictive models and performs advanced analytics.", "$100k–$130k/year"),
    ("Data Scientist", "Senior", "Leads data science initiatives and aligns analytics with business goals.", "$130k–$170k/year"),
    ("Solutions Architect", "Junior", "Assists in designing small system components and integrations.", "$90k–$110k/year"),
    ("Solutions Architect", "Mid-level", "Designs scalable systems and ensures integration with existing infrastructure.", "$110k–$140k/year"),
    ("Solutions Architect", "Senior", "Drives architecture strategy and oversees system design for large projects.", "$140k–$180k/year"),
    ("Automation Specialist", "Junior", "Identifies basic automation opportunities and builds simple workflows.", "$60k–$80k/year"),
    ("Automation Specialist", "Mid-level", "Develops and optimizes automation processes across teams.", "$80k–$100k/year"),
    ("Automation Specialist", "Senior", "Leads enterprise automation initiatives and evaluates RPA tools.", "$100k–$130k/year"),
    ("Change Management Consultant", "Junior", "Assists in training and communication for change initiatives.", "$65k–$85k/year"),
    ("Change Management Consultant", "Mid-level", "Plans and executes change strategies for projects.", "$85k–$110k/year"),
    ("Change Management Consultant", "Senior", "Develops change frameworks and leads large-scale transformation projects.", "$110k–$150k/year"),
    ("Operations Analyst", "Junior", "Performs process mapping and prepares reports on operational metrics.", "$55k–$75k/year"),
    ("Operations Analyst", "Mid-level", "Analyzes workflows and recommends efficiency improvements.", "$75k–$95k/year"),
    ("Operations Analyst", "Senior", "Drives operational strategy and implements large-scale process changes.", "$95k–$125k/year"),
    ("IT Support Specialist", "Junior", "Provides first-line technical support and resolves basic issues.", "$50k–$70k/year"),
    ("IT Support Specialist", "Mid-level", "Handles advanced troubleshooting and supports IT infrastructure.", "$70k–$90k/year"),
    ("IT Support Specialist", "Senior", "Leads IT support strategy and oversees critical issue resolutions.", "$90k–$120k/year"),
    ("AI/ML Engineer", "Junior", "Assists in training models and testing machine learning workflows.", "$85k–$105k/year"),
    ("AI/ML Engineer", "Mid-level", "Builds and deploys machine learning models and improves algorithms.", "$105k–$135k/year"),
    ("AI/ML Engineer", "Senior", "Leads AI/ML initiatives and integrates solutions into business processes.", "$135k–$175k/year"),
    ("Compliance Specialist", "Junior", "Reviews compliance requirements and prepares reports.", "$60k–$80k/year"),
    ("Compliance Specialist", "Mid-level", "Monitors compliance standards and ensures adherence.", "$80k–$110k/year"),
    ("Compliance Specialist", "Senior", "Develops compliance strategies and oversees regulatory alignment.", "$110k–$140k/year"),
    ("Integration Specialist", "Junior", "Supports basic API integrations and system connectivity tasks.", "$65k–$85k/year"),
    ("Integration Specialist", "Mid-level", "Designs and implements integrations for diverse systems.", "$85k–$115k/year"),
    ("Integration Specialist", "Senior", "Leads integration strategies and resolves complex system challenges.", "$115k–$150k/year"),
    ("Customer Success Manager (Internal Clients)", "Junior", "Assists in gathering feedback and communicating client needs.", "$55k–$75k/year"),
    ("Customer Success Manager (Internal Clients)", "Mid-level", "Ensures client satisfaction by managing expectations and deliverables.", "$75k–$100k/year"),
    ("Customer Success Manager (Internal Clients)", "Senior", "Oversees client relationships and aligns solutions with business goals.", "$100k–$130k/year"),
    ("Functional Manager", "Junior", "Supports departmental goals by managing specific functions and ensuring team alignment.", "$80k–$100k/year"),
    ("Functional Manager", "Mid-level", "Manages team operations, sets functional goals, and ensures alignment with organizational objectives.", "$100k–$130k/year"),
    ("Functional Manager", "Senior", "Leads multiple functional areas, develops strategies, and aligns cross-functional goals.", "$130k–$170k/year"),
    ("Power Platform Engineer", "Junior", "Assists in configuring and implementing Power Platform solutions under guidance.", "$70k–$90k/year"),
    ("Power Platform Engineer", "Mid-level", "Builds custom applications and integrations, optimizing existing solutions.", "$90k–$120k/year"),
    ("Power Platform Engineer", "Senior", "Leads Power Platform architecture, scaling solutions, and mentoring team members.", "$120k–$150k/year"),
    ("Power Platform Administrator", "Junior", "Manages user accounts, permissions, and basic maintenance tasks.", "$60k–$80k/year"),
    ("Power Platform Administrator", "Mid-level", "Oversees platform configurations, performance tuning, and policy enforcement.", "$80k–$100k/year"),
    ("Power Platform Administrator", "Senior", "Designs administrative strategies, implements advanced security measures, and leads governance policies.", "$100k–$130k/year"),
    ("Power Platform Developer", "Junior", "Creates basic Power Apps, flows, and low-complexity customizations.", "$65k–$85k/year"),
    ("Power Platform Developer", "Mid-level", "Builds advanced Power Platform applications and integrates with external systems.", "$85k–$115k/year"),
    ("Power Platform Developer", "Senior", "Leads complex development projects, including ALM, and optimizes performance across the Power Platform.", "$115k–$145k/year"),
    ("Power Platform Tester", "Junior", "Performs manual testing for Power Platform applications and logs defects.", "$55k–$75k/year"),
    ("Power Platform Tester", "Mid-level", "Develops test scripts and performs automation testing for Power Platform solutions.", "$75k–$95k/year"),
    ("Power Platform Tester", "Senior", "Defines test strategies, oversees test automation, and ensures testing standards across projects.", "$95k–$125k/year"),    
    ("Director of Technology and Operations", "Senior", "Oversees technical solutions and operational efficiency across teams.", "$150k–$200k/year"),
    ("Director of Software Solutions", "Senior", "Leads software development, integration, and internal operational support.", "$150k–$200k/year"),
    ("Director of Business Applications", "Senior", "Manages enterprise systems like Power Platform and supports operational tools.", "$150k–$200k/year"),
    ("Director of Digital Transformation", "Senior", "Drives innovation, automation, and technological advancement across the business.", "$160k–$210k/year"),
    ("Director of Enterprise Solutions", "Senior", "Oversees large-scale solutions and system integrations across departments.", "$160k–$210k/year"),
    ("Director of Engineering and Operations", "Senior", "Combines engineering leadership with operational oversight for internal tools.", "$150k–$200k/year"),
    ("Senior Director of Technology Enablement", "Senior", "Enables business success through strategic technology leadership.", "$170k–$220k/year"),
    ("Director of Service Delivery", "Senior", "Ensures the successful delivery of technology and operational services, meeting quality, timeliness, and client satisfaction goals.", "$150k–$200k/year")
]

# Save the data to a CSV file
file_path = "C:/Users/conta/Downloads/team career program/roles_and_compensation.csv"
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(roles)

file_path
