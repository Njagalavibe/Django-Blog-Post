

⦁ Portfolio: Blog & Project Showcase
    A modern Django-based portfolio website that combines a technical blog with a project showcase featuring Google OAuth authentication and interactive content.

⦁ Project Overview
    This application serves as both a learning journal and professional portfolio, built with Django to demonstrate full-stack development skills. The platform allows for blog posts documenting learning journeys while showcasing completed projects with technical details.

⦁ Features
    Blog System:
        Draft/Published Workflow: Save posts as drafts before publishing
        SEO-Optimized URLs: Auto-generated slugs for better search visibility
        Rich Content Management: Full-text posts with featured excerpts
        Scheduled Publishing: Control publication dates for content planning

⦁ Portfolio Projects:
    Project Showcase: Display projects with images, descriptions, and tech stacks
    Live Demos & Code: Direct links to GitHub repositories and live deployments
    Featured Projects: Highlight key projects on the homepage
    Technology Tags: Display used technologies for easy filtering

⦁ User Interaction:
    Google OAuth Authentication: Secure login via Google accounts
    Comment System: Authenticated users can comment on blog posts
    Like/Dislike Reactions: Interactive feedback system
    User Profiles: Basic user information for comment attribution

⦁ Admin Features:
    Custom Admin Interface: Enhanced Django admin with better filtering and search
    Auto-Slug Generation: Automatic URL creation from post titles
    Media Management: Image upload and management for projects
    Content Moderation: Full control over posts, comments, and user interactions

⦁ Technology Stack
    Backend:
        Django 4.x: Main web framework
        Django AllAuth: Authentication with Google OAuth
        Pillow: Image processing for project screenshots
        SQLite: Development database (easy to switch to PostgreSQL for production)

⦁ Frontend (Planned):
    HTML5/CSS3: Semantic markup and styling
    Bootstrap 5: Responsive design framework
    JavaScript: Interactive elements and form validation

⦁ Development Tools:
    Git: Version control
    Virtual Environment: Python dependency isolation
    Django Debug Toolbar: Development assistance

⦁ Project Structure:

Portfolio/
├── blog/                          # Main Django application
│     migrations/                # Database migrations
│     templates/blog/           # HTML templates
│     __init__.py
│     admin.py                  # Custom admin configuration
│     apps.py
│     models.py                 # Post, Comment, Like, Project models
│     tests.py
│     urls.py                   # App URL routing
│     views.py                  # View functions and classes
├── portfolio_project/               # Django project settings
│     __init__.py
│     asgi.py
│     settings.py              # Project configuration
│     urls.py                  # Main URL routing
│     wsgi.py
├── static/                       # CSS, JavaScript, images
│     css/
│     js/
├── media/                        # User-uploaded files
│      blog_images/
│      project_images/
├── requirements.txt             # Python dependencies
├── manage.py                    # Django management script
└── README.md                    # This file

⦁ Installation Guide
    Prerequisites
    Python 3.8 or higher
    Git
    Google account (for OAuth setup)
    Installation
    Clone this repository
    Create vitual enviroment
    Activate enviroment
    Install requirements 
    Run migrations
    Create Super User
    Run server

⦁ Usage Guide
    For Blog Readers
    Browse blog posts on the home page
    Click any post to read full content
    Sign in with Google to comment or react to posts
    View project portfolio in the projects section

⦁ Development Roadmap
    Completed ✅
        Core Django models (Post, Comment, Like, Project)
        Custom admin interface
        Database schema with relationships
        Slug-based URLs for SEO

⦁ In Progress 
    Google OAuth integration
    URL patterns and views
    HTML templates and frontend design
    Comment and like functionality

⦁ Planned
    Responsive mobile design
    Email notifications for new comments
    Advanced search functionality
    Project filtering by technology
    RSS feed for blog posts
    Social media sharing
    Analytics integration
    Deployment to cloud platform (Not yet sure which to use)

⦁ Contributing
    While this is primarily a personal portfolio project, suggestions and improvements are welcome:
    Fork the repository
    Create a feature branch (git checkout -b feature/improvement)
    Commit changes (git commit -m 'Add some improvement')
    Push to branch (git push origin feature/improvement)
    Open a Pull Request

⦁ License   
     This project is open source and available under the MIT License.

⦁ Author
    Lumu Patrick / NjagalaVibe

GitHub: https://github.com/Njagalavibe

Portfolio: still working on it

⦁ Acknowledgments
    Django community for excellent documentation
    Google for OAuth authentication services
    All open-source libraries used in this project
    Note: This project is actively developed as part of a learning journey. Features and structure may evolve as new technologies and best practices are learned.

