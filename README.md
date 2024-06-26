![Logo]()

I'm excited to share with you to You Matter, a fictional blog website developed using Django Framework as part of Portfolio Project 4. 

## Project Overview

Welcome to "You Matter" – a transformative project dedicated to mental health support and fostering community connections. Imagine a place where understanding flourishes, and empathy turns challenges into victories. As a mental health practitioner, my goal is not just to build a website, but to create a space for people seeking support and connection.

![Hero Page]() 

----

## [Content](#content)
- [Aims and Objectives](#aims-objectives)
- [Agile Development Process](#agile-development-process)
    - [User Stories](#user-stories)
    - [Target Audience](#target)
    - [Age Group and Region](#age-region)
    - [User Personas](#user-personas)
     - [First Time Visitor](#first-time-visitor)
     - [Returning Visitor](#returning-visitor)
     - [Frequent Visitor](#frequent-visitor)
  - [Design](#design)
    - [Wireframes: Figma VS Final version](#wireframes)
    - [Brand & Logo: Canva ](#brand)
    - [Colour Palette: Canva ](#colour)
    - [Typography: Google font / Bootstrap ](#typography)
  - [Desktop, Tablet, Mobile Responsiveness](#responsiveness)
  - [Features](#features)
    - [Future Features](#future)   
  - [Database Control Flow](#database)
   - [Django Admin](#admin)
  - [Testing](#testing)
      - [CSS Validation](#validation)
      - [Python CI Testing ](#tythontesting )
      - [Lighthouse](#manual-testing)
      - [Bugs](#bugs)
- [Technologies Used](#testing)
  - [Credits](#credits)
  - [Acknowledgement](#acknowledgement)

-----

## Aims and Objectives
1. **Providing Accessible Mental Health Resources**

- Offer a wide range of articles, videos, and tools to educate and support individuals in their mental health journey.
- Ensure resources are easily accessible and presented in a user-friendly manner.

2. **Fostering a Supportive Community**

- Create a safe and welcoming environment where individuals can share their stories, experiences, and challenges.
- Encourage peer support through forums, discussion groups, and community events.

3. **Empowering Individuals**

- Raise awareness about various mental health conditions and the importance of seeking help.
- Advocate for the reduction of stigma surrounding mental health issues through education and open dialogue.

4. **Connecting People to Professional Support**

- Offer directories and referrals to mental health professionals for those seeking personalized care.
- Provide information on how to access crisis support and emergency services when needed.

5. **Encouraging Continuous Learning and Growth**

- Facilitate ongoing learning through webinars, workshops, and expert talks.
- Promote the latest research and developments in mental health care and wellness.

## Agile Development Process

In developing "You Matter," we have utilized an Agile methodology, specifically employing the Kanban board feature in GitHub. This approach allows us to:

- **Highlight Must-Haves, Could-Haves, and More**: Clearly categorize and prioritize tasks and features based on their importance and impact.
- **Track Progress**: Continuously monitor the project's development and adjust priorities as needed.
- **Add Issues on the Go**: Dynamically create and manage issues as they arise, ensuring that all aspects of the project are addressed in a timely manner.
- **User Story Statements**: Each issue includes a user story statement to clarify the goal and context, ensuring that all team members have a shared understanding of the task at hand.

![Kanban Board]() 

### Example User Stories

As a site user, I want to:

1. **Access Mental Health Blogs**
   - *User Story*: As a user, I want to read blog posts that highlight different mental health topics and subjects so that I can stay informed and find relevant information.
2. **Subscribe to a Newsletter**
   - *User Story*: As a user, I want to subscribe to a newsletter to receive regular updates and insights on mental health topics.
3. **Connect with Community Events**
   - *User Story*: As a user, I want to find and connect with community events to engage with others and participate in supportive activities.
4. **Log In and Write Posts**
   - *User Story*: As a user, I want to log in and write my own posts to share my experiences and thoughts on mental health.
5. **Comment on Posts**
   - *User Story*: As a user, I want to comment on blog posts and other users' posts to engage in discussions and offer support.
6. **Delete My Posts**
   - *User Story*: As a user, I want to delete my own posts if I no longer want them to be visible.
7. **Access Crisis Contact Information**
   - *User Story*: As a user, I want to easily find crisis contact information so that I can get immediate help if needed.

### Target Audience

"You Matter" is designed to support and connect the following groups:

1. **Individuals Seeking Mental Health Resources**
   - People looking for reliable information and resources on mental health topics.
2. **Community Members Seeking Support**
   - Individuals who want to engage with a supportive community and share their experiences.
3. **Mental Health Advocates**
   - Those who are passionate about raising awareness and reducing the stigma around mental health issues.
4. **People in Crisis**
   - Individuals in need of immediate help and information on crisis support.
5. **Family and Friends of Those Struggling with Mental Health**
   - Loved ones looking for resources and ways to support their friends or family members.
6. **Mental Health Professionals**
   - Therapists, counselors, and other professionals seeking to connect with the community and provide their expertise.

### Age Group and Region

- **Age Group**: Our platform caters to individuals aged 16 and above.
- **Region**: While our online resources are available worldwide, onsite support is UK-based. We offer virtual chat help but recommend that users also check with local experts and not rely solely on online assistance.

## User Persona

In this section, I used UserPersona.dev free AI-powered User Persona Generator. By offering a concise description, it generates insightful user personas. The narratives presented below are inspired by real-life struggles, with due consideration given to privacy and protection through the alteration of names, locations, image and ages. 

- Story 1: Sarah (Teenager)

![User1](youmatter/media/shop_images/sarah-userpersona.png) 

Sarah is a 17-year-old high school student who has been struggling with social anxiety. She often felt isolated and overwhelmed in crowded social situations, which affected her academic performance and overall well-being. One day, she stumbled upon the "You Matter" website, where she found articles and self-help resources specifically tailored to teenagers facing similar challenges. She joined a support group and gradually built the confidence to share her experiences. Through the encouragement and guidance of the group, Sarah learned strategies to manage her anxiety and discovered that she wasn't alone in her struggles. Today, Sarah is thriving in school and is excited about the future, thanks to the support and resources she found on the website.

- Story 2: Michael (Working Professional)

![User2](youmatter/media/shop_images/michael-userpersona.png) 

Michael, a 35-year-old working professional, had been dealing with work-related stress, anxiety, and burnout for years. He felt overwhelmed and on the brink of quitting his job. After a particularly tough week, he decided to search for mental health support online and came across the "You Matter" website. The resources on stress management, work-life balance, and burnout prevention resonated with him. He started using the self-assessment tools and strategies provided, which helped him regain control over his mental health. Michael also found an online support group for professionals in similar situations. With the support and insights he gained from the community, he made significant changes in his life and career, ultimately finding a better work-life balance and improved mental well-being.

- Story 3: Margaret (Retired Senior)

![User3](youmatter/media/shop_images/margaret-userpersona.png) 

Margaret, an 80-year-old retiree, had been feeling increasingly lonely and anxious after losing her spouse and dealing with the challenges of aging. She discovered the "You Matter" website through her grandson and found a wealth of resources tailored to seniors facing mental health issues. The website provided information on coping with grief and isolation and tips for maintaining emotional well-being in later life. Margaret also joined an online seniors' support group where she met fellow retirees facing similar challenges. The connections she made and the compassionate discussions helped her combat her feelings of loneliness and find joy in her golden years. Margaret's experience demonstrates that it's never too late to seek support and that "You Matter" is there for people of all ages.

Testimonial 1:
" 'You Matter' changed my life. It's a sanctuary for teens like me with social anxiety. This place truly cares."

Testimonial 2:
" 'You Matter' saved my career. The resources and support here gave me control over my stress. It's a lifesaver."

Testimonial 3:
"At 80, I found joy again with 'You Matter.' The resources and support group keep me going. It's never too late to seek help."


# Bugs and Fixes

I encountered challenges typical of a beginner in Django development, including initial configuration errors and syntax issues. 
More complex issues arose from version discrepancies and environment configurations. Below are some examples listed:

| **1. Fix Heroku functionality by adding dependencies to requirements.txt and configuring Procfile** | 
  - Added necessary dependencies to `requirements.txt` for Heroku deployment.
  - Configured `Procfile` for correct execution on Heroku.
  - Opened workspace from Gitpod instead of GitHub directly.
  - Refreshed workspace until correct dependencies loaded. |

| **2. Modify runtime.txt to improve compatibility with Heroku** | 
  - Updated Python version from 3.8.15 to 3.10.14 for Heroku compatibility. |

| **3. Fix `post_detail` view in index and convert it back to a function-based view** | 
  - Restored functionality using a function-based view for `post_detail` rendering. |

| **4. Re-added Procfile multiple times due to it disappearing, a Gitpod issue** | 
  - Opened workspace from Gitpod instead of GitHub directly.
  - Refreshed workspace to ensure correct dependencies applied. |

| **5. Fixed `post_detail` view to correctly retrieve and display individual blog** | 
  - Refactored to fetch `Post` object with specific slug and status in view. |

| **6. Fix login issue** | 
  - Modified edit button conditional rendering for authenticated users.
  - Adjusted script inclusion in extras block for functionality.
  - Updated head title block for signup page using translation tags.
  - Added `comments.js` for necessary functionality. |

| **7. Fix `sign_up.html`** | 
  - Modified `signup.html` to extend `base.html` for consistent styling.
  - Updated head title block for signup page using translation tags.
  - Corrected ending block tag for proper content closure. |

| **8. Fix newsletter app** | 
  - Updated `about.html` to include newsletter signup link or section.
  - Adjusted `newsletter_signup.html` to extend `base.html` with signup form.
  - Added path for newsletter signup in `urls.py` to route requests correctly.
  - Implemented `newsletter_signup` view in `views.py` for signup handling.
  - Modified `base.html` for navigation/footer links related to newsletter.
  - Ensured `urls.py` includes all paths for newsletter functionality. |

| **9. Fix newsletter submission form** | 
  - Updated `connect_view` for form submission handling and success messages.
  - Ensured `connect.html` displays form and handles success message. |

| **10. Resolving Issues After Transitioning to a New Gitpod Workspace** | 
  - Addressed issues after transitioning to new Gitpod workspace.
  - Updated Django settings for CSRF trusted origins and allowed hosts.
  - Reinstalled dependencies to ensure correct environment setup. |

| **11. Enhancements in Form Handling and Image Upload Integration** | 
  - Modified `CommentForm` to handle featured image uploads.
  - Implemented image resizing and upload using Cloudinary.
  - Added validation for image size limitations.
  - Converted resized image to `BytesIO` for efficient storage.
  - Updated `resize_image` function for PIL-based image resizing.
  - Enhanced `PostDeleteView` for improved form validation and error handling. |




