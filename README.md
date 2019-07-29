# TTH_TD_Project_8
 Filtering and Searching the Mineral Catalog

In project #8 We added search and filtering functions to our final version of Project #6
which we built with the Django Web Framework. 

The site has a database of 800+ minerals. Each mineral is a an instance of the
Mineral Model. There is a detail page to look at all of it's attributes. There is also a
random button to take you to any mineral at random. It's always a asurprise! 

In addition to the features of Project #6. I have added a search bar that lets you type
any string, and it will pull any mineral that might have a matching string in any of it's
fields. All fields will be listed below. There are also links with all the letters of the
alphabet that will pull all the minerals that begin with the chosen letter and display
them on the home page. In addition to the "search by letter" function there are 2 similar
functions, "search by group" and "search by diaphaneity." These 2 other functions pull
results relating to their group and diaphaneit. 

NOTE: Clicking any letter, group, or diaphaneity will bolden and underline the letter
as a visual signal to the user. This will let them know what they have clicked. The
URL has also been made to be as easily read as possible. 

Also, check the "site_preview_images_and_coverage" folder to see previews of the site
and coverage.

-----------------------------------------
Fields

* name
* image_filename
* image_caption
* category
* formula
* strunz_classification
* color
* crystal_system
* unit_cell
* crystal_symmetry
* cleavage
* mohs_scale_hardness
* luster
* streak
* diaphaneity
* optical_properties
* refractive_index
* crystal_habit
* specific_gravity
* group

-----------------------------------------

Check requirements.txt Info on package versions on it.

* coverage==4.5.3
* Django==2.2.3
* django-debug-toolbar==2.0
* pytz==2019.1
* sqlparse==0.3.0

-----------------------------------------

Check test coverage

* coverage run --source='.' manage.py test minerals
* coverage report