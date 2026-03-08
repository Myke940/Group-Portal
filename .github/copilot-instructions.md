# Group Portal - AI Agent Instructions

## Project Overview

**Group Portal** is a Django 4.2 web application designed to facilitate group collaboration with user profiles, forums, and shared materials. It follows a modular architecture with three main Django apps: `core` (user & group management), `forum`, and `matireals` (materials/resources).

## Architecture & Component Boundaries

### Core Data Model
- **Userprofile**: Extends Django's `User` model with profile pictures, role-based access (student/instructor/admin), and bio
- **GroupProfile**: Represents a collaborative group with members, description, logo, and creation timestamp
- **Relationship**: Groups have many-to-many membership with Userprofiles

### App Structure
- **core/** - Group and user profile management (active endpoints)
- **forum/** - Forum discussion features (models empty, under development)
- **matireals/** - Shared materials/resources (models empty, under development)
- **group_portal/** - Project configuration (Django settings, root URL routing)

### Frontend Architecture
- **Base template** (`templates/base.html`): Bootstrap 5.3 navbar with navigation to Forum, Group, Votes, Announcements, Materials, and Members
- **Role-based navigation**: Conditionally shows "Log in/Sign up" or "View Profile/Log out" based on `user.is_authenticated`
- **Template inheritance**: Child templates extend `base.html` with `{% block content %}`
- **Static assets**: CSS in `staticfiles/css/static.css`, images in `static/pictures/` (group logos, profile pics)

## Critical Development Workflows

### Running the Development Server
```bash
python manage.py runserver
```
Django runs on `http://localhost:8000` with SQLite3 database.

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
Migrations are tracked in each app's `migrations/` folder (e.g., `core/migrations/0001_initial.py`).

### Admin Panel
Access at `/admin/` after creating a superuser:
```bash
python manage.py createsuperuser
```

## Project-Specific Patterns & Conventions

### View Pattern: Class-Based Views (CBV)
All views use Django's generic CBVs:
```python
# Example: core/views.py
class UserProfileView(DetailView):
    model = Userprofile
    template_name = 'core/userprofile.html'
    context_object_name = 'userprofile'  # Variable name in template
    def get_object(self):
        return self.request.user.userprofile  # Always fetch logged-in user's profile
```
- Use `DetailView` for single object display
- Override `get_object()` for custom retrieval logic (e.g., accessing `request.user`)
- Template context uses `context_object_name` for template variables

### Model Conventions
- Use `models.CharField(max_length=X)` with explicit max_length
- Use `ForeignKey(on_delete=models.CASCADE)` with explicit cascade behavior
- Use `blank=True, null=True` for optional fields
- Define `__str__()` method for readable admin/debugging output
- Use `auto_now_add=True` for creation timestamps (immutable)

### URL Routing
- Root URLs defined in `group_portal/urls.py` (main entry point)
- App URLs defined in each app's `urls.py` (e.g., `core/urls.py`)
- Include app URLs: `path('', include('core.urls'))`
- Name all patterns for use in templates: `{% url 'user-profile' %}`

### Media File Handling
- Profile pictures: `ImageField(upload_to='profile_pics/', null=True, blank=True)`
- Group logos: `ImageField(upload_to='group_logos/', null=True, blank=True)`
- URL in templates: `{{ object.image_field.url }}`
- Static files configured in `group_portal/settings.py` with `STATIC_URL = '/static/'`

### Template Patterns
- Extend `base.html` for consistent navigation
- Use `{% if condition %}` for conditional rendering (e.g., auth checks)
- Use Bootstrap 5.3 classes for styling (cards, images, flexbox)
- Use Django template tags: `{{ variable }}`, `{% url 'name' %}`, `{% block name %}`

## Integration Points & External Dependencies

### Third-Party CSS
- Bootstrap 5.3 via CDN (in `base.html`)
- Provides responsive navbar, card components, grid system

### Django Contrib Apps
- `django.contrib.auth` - User authentication (used by Userprofile)
- `django.contrib.admin` - Admin interface for managing models
- `django.contrib.sessions` - Session middleware for user tracking
- `django.contrib.messages` - Flash message framework

### Database
- SQLite3 (`db.sqlite3`) - Development database
- File-based, no external DB server required
- Migrations auto-applied via `manage.py migrate`

## Code Examples & Key Files

### Creating a New View
Reference [core/views.py](core/views.py#L1) for the DetailView pattern. To add a new endpoint:
1. Create view class in the app's `views.py`
2. Register in app's `urls.py` with `path()` and unique `name`
3. Create template in `templates/app_name/template.html`

### Adding Model Fields
Reference [core/models.py](core/models.py#L1) - all fields include `max_length`, `on_delete`, and `null/blank` parameters for clarity.

### Extending Authentication
Reference [core/models.py](core/models.py#L7) - `Userprofile` extends Django's `User` with OneToOneField and uses role choices for role-based access control (RBAC).

## Known Issues & Incomplete Features

- **Forum & Materials apps**: Models empty - scaffold endpoints and templates following core app pattern
- **Missing endpoints**: "Edit Profile", "Logout", Forum, Announcements not yet implemented
- **No migrations**: Forum and Materials apps have empty migrations
- **No form handling**: No forms.py files - implement model forms for create/update operations
- **Typo**: App named `matireals` instead of `materials`

## AI Agent Recommendations

1. **When adding features**: Follow CBV pattern (DetailView, ListView, CreateView) - don't use function-based views
2. **When modifying models**: Always create and apply migrations; test with `python manage.py migrate`
3. **When working with auth**: Access current user via `self.request.user` in CBVs; extend Userprofile for user data
4. **When building forms**: Use Django ModelForms to auto-generate forms from models
5. **When adding templates**: Extend base.html, use Bootstrap utility classes, test with development server
