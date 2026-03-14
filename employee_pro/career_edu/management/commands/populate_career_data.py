from django.core.management.base import BaseCommand
from career_edu.models import CareerPath, EducationResource


CAREER_DATA = [
    {
        'title': 'Software Engineer',
        'domain': 'technology',
        'description': 'Design, develop, and maintain software systems and applications. '
                       'Work with teams to build scalable, reliable software solutions.',
        'required_skills': 'Python, JavaScript, Data Structures, Algorithms, Git, Problem Solving',
        'avg_salary': '$90,000 - $150,000',
        'growth_outlook': 'Very High (25% growth by 2030)',
        'icon': 'code-slash',
    },
    {
        'title': 'Data Scientist',
        'domain': 'technology',
        'description': 'Analyze complex data sets to help organizations make data-driven decisions. '
                       'Build machine learning models and extract valuable insights.',
        'required_skills': 'Python, R, Machine Learning, Statistics, SQL, Data Visualization',
        'avg_salary': '$95,000 - $160,000',
        'growth_outlook': 'Very High (36% growth by 2031)',
        'icon': 'graph-up',
    },
    {
        'title': 'Cloud Architect',
        'domain': 'technology',
        'description': 'Design and oversee cloud computing strategies, solutions, and infrastructure. '
                       'Ensure security, scalability, and cost-effectiveness of cloud platforms.',
        'required_skills': 'AWS, Azure, GCP, Networking, Security, DevOps, Linux',
        'avg_salary': '$120,000 - $180,000',
        'growth_outlook': 'High (28% growth by 2030)',
        'icon': 'cloud',
    },
    {
        'title': 'UX/UI Designer',
        'domain': 'arts',
        'description': 'Create intuitive, engaging user interfaces and experiences. '
                       'Research user needs and translate them into beautiful, functional designs.',
        'required_skills': 'Figma, Adobe XD, User Research, Prototyping, CSS, Design Thinking',
        'avg_salary': '$70,000 - $120,000',
        'growth_outlook': 'High (13% growth by 2030)',
        'icon': 'palette',
    },
    {
        'title': 'Product Manager',
        'domain': 'business',
        'description': 'Lead the development of products from conception to launch. '
                       'Bridge engineering, design, and business stakeholders.',
        'required_skills': 'Strategy, Communication, Agile, Data Analysis, Leadership, Roadmapping',
        'avg_salary': '$100,000 - $170,000',
        'growth_outlook': 'High (10% growth by 2030)',
        'icon': 'kanban',
    },
    {
        'title': 'Cybersecurity Analyst',
        'domain': 'technology',
        'description': 'Protect organizations from cyber threats. Monitor, detect, '
                       'and respond to security incidents and vulnerabilities.',
        'required_skills': 'Network Security, Ethical Hacking, SIEM, Python, Risk Assessment, Compliance',
        'avg_salary': '$85,000 - $140,000',
        'growth_outlook': 'Very High (35% growth by 2031)',
        'icon': 'shield-lock',
    },
    {
        'title': 'Financial Analyst',
        'domain': 'finance',
        'description': 'Analyze financial data to support business decisions, investments, '
                       'and budgeting. Create models and reports for stakeholders.',
        'required_skills': 'Excel, Financial Modeling, Accounting, SQL, PowerBI, Communication',
        'avg_salary': '$65,000 - $110,000',
        'growth_outlook': 'Moderate (9% growth by 2030)',
        'icon': 'currency-dollar',
    },
    {
        'title': 'Digital Marketing Manager',
        'domain': 'marketing',
        'description': 'Plan and execute digital marketing campaigns across various channels. '
                       'Drive brand awareness, lead generation, and customer engagement.',
        'required_skills': 'SEO, SEM, Social Media, Content Marketing, Analytics, Email Marketing',
        'avg_salary': '$60,000 - $110,000',
        'growth_outlook': 'High (10% growth by 2030)',
        'icon': 'megaphone',
    },
    {
        'title': 'Healthcare Administrator',
        'domain': 'healthcare',
        'description': 'Manage and coordinate healthcare services and facilities. '
                       'Ensure efficient operations and high-quality patient care.',
        'required_skills': 'Healthcare Regulations, Leadership, Budgeting, Communication, EHR Systems',
        'avg_salary': '$70,000 - $120,000',
        'growth_outlook': 'High (28% growth by 2030)',
        'icon': 'hospital',
    },
    {
        'title': 'Machine Learning Engineer',
        'domain': 'technology',
        'description': 'Build and deploy machine learning models at scale. '
                       'Bridge research and production to create AI-powered products.',
        'required_skills': 'Python, TensorFlow, PyTorch, MLOps, Cloud Platforms, Mathematics',
        'avg_salary': '$110,000 - $175,000',
        'growth_outlook': 'Very High (40% growth by 2031)',
        'icon': 'cpu',
    },
]

RESOURCE_DATA = [
    {
        'title': 'The Complete Python Bootcamp',
        'provider': 'Udemy',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'technology',
        'description': 'Learn Python programming from scratch. Covers fundamentals, OOP, data structures, '
                       'and real-world projects. Perfect for beginners.',
        'url': 'https://www.udemy.com/course/complete-python-bootcamp/',
        'duration': '22 hours',
        'is_free': False,
        'skills_covered': 'Python, OOP, Data Structures, Problem Solving',
        'careers': ['Software Engineer', 'Data Scientist', 'Machine Learning Engineer'],
    },
    {
        'title': 'AWS Cloud Practitioner Essentials',
        'provider': 'AWS Training',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'technology',
        'description': 'Foundational understanding of AWS Cloud concepts, services, security, '
                       'architecture, pricing, and support.',
        'url': 'https://aws.amazon.com/training/learn-about/cloud-practitioner/',
        'duration': '6 hours',
        'is_free': True,
        'skills_covered': 'AWS, Cloud Computing, Security, Architecture',
        'careers': ['Cloud Architect', 'Software Engineer'],
    },
    {
        'title': 'Machine Learning Specialization',
        'provider': 'Coursera (Andrew Ng)',
        'resource_type': 'course',
        'difficulty': 'intermediate',
        'domain': 'technology',
        'description': 'Master the fundamentals of machine learning and build real-world AI applications. '
                       'Taught by Stanford professor Andrew Ng.',
        'url': 'https://www.coursera.org/specializations/machine-learning-introduction',
        'duration': '3 months',
        'is_free': False,
        'skills_covered': 'Machine Learning, Python, Regression, Neural Networks, Decision Trees',
        'careers': ['Data Scientist', 'Machine Learning Engineer'],
    },
    {
        'title': 'Google UX Design Professional Certificate',
        'provider': 'Coursera (Google)',
        'resource_type': 'certification',
        'difficulty': 'beginner',
        'domain': 'arts',
        'description': 'Learn the foundations of UX design, including empathizing with users, '
                       'building wireframes and prototypes, and conducting research.',
        'url': 'https://www.coursera.org/professional-certificates/google-ux-design',
        'duration': '6 months',
        'is_free': False,
        'skills_covered': 'UX Design, Figma, Prototyping, User Research, Design Thinking',
        'careers': ['UX/UI Designer'],
    },
    {
        'title': 'Introduction to Cybersecurity',
        'provider': 'Cisco Networking Academy',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'technology',
        'description': 'Explore the world of cybersecurity and learn how to protect digital information. '
                       'Perfect starting point for aspiring security professionals.',
        'url': 'https://skillsforall.com/course/introduction-to-cybersecurity',
        'duration': '15 hours',
        'is_free': True,
        'skills_covered': 'Cybersecurity, Network Security, Risk Management',
        'careers': ['Cybersecurity Analyst'],
    },
    {
        'title': 'Financial Markets',
        'provider': 'Coursera (Yale University)',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'finance',
        'description': 'An overview of the ideas, methods, and institutions that permit human society '
                       'to manage risks and foster enterprise.',
        'url': 'https://www.coursera.org/learn/financial-markets-global',
        'duration': '7 weeks',
        'is_free': True,
        'skills_covered': 'Financial Markets, Investment, Risk Management, Portfolio Theory',
        'careers': ['Financial Analyst'],
    },
    {
        'title': 'Digital Marketing Fundamentals',
        'provider': 'Google Digital Garage',
        'resource_type': 'certification',
        'difficulty': 'beginner',
        'domain': 'marketing',
        'description': 'Learn the fundamentals of digital marketing with this free certification '
                       'from Google. Covers SEO, SEM, social media, and analytics.',
        'url': 'https://learndigital.withgoogle.com/digitalgarage',
        'duration': '40 hours',
        'is_free': True,
        'skills_covered': 'SEO, SEM, Social Media Marketing, Email Marketing, Analytics',
        'careers': ['Digital Marketing Manager'],
    },
    {
        'title': 'Product Management Fundamentals',
        'provider': 'LinkedIn Learning',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'business',
        'description': 'Learn the core skills needed to become a successful product manager. '
                       'Covers roadmapping, prioritization, stakeholder management, and Agile.',
        'url': 'https://www.linkedin.com/learning/product-management-first-steps',
        'duration': '8 hours',
        'is_free': False,
        'skills_covered': 'Product Strategy, Roadmapping, Agile, User Stories, Prioritization',
        'careers': ['Product Manager'],
    },
    {
        'title': 'Statistics and Data Science MicroMasters',
        'provider': 'edX (MIT)',
        'resource_type': 'certification',
        'difficulty': 'advanced',
        'domain': 'technology',
        'description': 'Master the foundations of data science, statistics, and machine learning. '
                       'Designed by MIT faculty for aspiring data scientists.',
        'url': 'https://www.edx.org/micromasters/mitx-statistics-and-data-science',
        'duration': '1 year',
        'is_free': False,
        'skills_covered': 'Statistics, Probability, Machine Learning, Data Analysis, R, Python',
        'careers': ['Data Scientist', 'Machine Learning Engineer'],
    },
    {
        'title': 'The Web Developer Bootcamp',
        'provider': 'Udemy',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'technology',
        'description': 'The only course you need to learn web development. '
                       'Covers HTML, CSS, JavaScript, Node.js, and more.',
        'url': 'https://www.udemy.com/course/the-web-developer-bootcamp/',
        'duration': '63 hours',
        'is_free': False,
        'skills_covered': 'HTML, CSS, JavaScript, Node.js, MongoDB, Bootstrap',
        'careers': ['Software Engineer', 'UX/UI Designer'],
    },
    {
        'title': 'Healthcare Administration Essentials',
        'provider': 'edX',
        'resource_type': 'course',
        'difficulty': 'beginner',
        'domain': 'healthcare',
        'description': 'Learn the fundamentals of healthcare management, including policy, '
                       'finance, quality improvement, and leadership in healthcare settings.',
        'url': 'https://www.edx.org/',
        'duration': '4 weeks',
        'is_free': True,
        'skills_covered': 'Healthcare Management, Policy, Leadership, Quality Improvement',
        'careers': ['Healthcare Administrator'],
    },
    {
        'title': 'AWS Solutions Architect Associate',
        'provider': 'A Cloud Guru',
        'resource_type': 'certification',
        'difficulty': 'intermediate',
        'domain': 'technology',
        'description': 'Prepare for the AWS Solutions Architect Associate certification. '
                       'Gain hands-on experience designing and deploying systems on AWS.',
        'url': 'https://acloudguru.com/course/aws-certified-solutions-architect-associate-saa-c03',
        'duration': '40 hours',
        'is_free': False,
        'skills_covered': 'AWS, Cloud Architecture, EC2, S3, VPC, IAM, RDS',
        'careers': ['Cloud Architect', 'Software Engineer'],
    },
]


class Command(BaseCommand):
    help = 'Populate the database with initial career and education data'

    def handle(self, *args, **options):
        self.stdout.write('Creating career paths...')
        career_map = {}
        for data in CAREER_DATA:
            career, created = CareerPath.objects.get_or_create(
                title=data['title'],
                defaults={
                    'domain': data['domain'],
                    'description': data['description'],
                    'required_skills': data['required_skills'],
                    'avg_salary': data['avg_salary'],
                    'growth_outlook': data['growth_outlook'],
                    'icon': data['icon'],
                }
            )
            career_map[career.title] = career
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'  {status}: {career.title}')

        self.stdout.write('Creating education resources...')
        for data in RESOURCE_DATA:
            career_titles = data.pop('careers', [])
            resource, created = EducationResource.objects.get_or_create(
                title=data['title'],
                defaults={k: v for k, v in data.items()}
            )
            for title in career_titles:
                if title in career_map:
                    resource.career_paths.add(career_map[title])
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'  {status}: {resource.title}')

        self.stdout.write(self.style.SUCCESS('Successfully populated career and education data!'))
