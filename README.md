<h1>AutoResumed</h1>

In the modern era resumes are suppose to be customtalored to the job you are applying to. But, In todays market the way to apply to jobs is to apply on mass. These two things are seemingly contradictory and a tedious and ever growing time sync. 

Autoresumed is a project to add tags to aspects of a resume so that people can generate and customizes a resume to the job your applying to simply by selecting all relevent tags within a resume to allow for easy generation. Inspired by and dependent upon JSON Resume https://jsonresume.org/ and its reimagined commandline tool resumed by rbardini.

Currently A comprehensive web application for managing multiple user's resume data and producing resumes via tag selection. Soon to be a CLI tool aswell. 

Check out our tagged-resume.json to understand the tag-wrapped schema we implement to generate JSON Resume complient resumes.

<h1>Dependencies</h1>
Python Prisma client<br>
Flask<br>
postgres<br>
react<br>
JSON Resume - https://jsonresume.org/<br>
resumed - https://github.com/rbardini/resumed/<br>

## Challenges we ran into
Fleshing out this database was a nightmare, creddit to Quinn on that one. His work in ironing out this extensive and verbose system was intense. 

## Accomplishments that we're proud of
Many pivots and shifts have lead this project to quite the undertaking. At current the CLI has been mostly stripped down in favor of a web interface. Many late nights and many constant hours have lead this to be the project it is today. 

## What we learned
Databases are quite a lot. Its clearer how people can work on them as a job exclusivly. a good reminder that the only bug free code is the code you dont write. Along with the usual "the internet is held together by duct tape" we get our own appriciation for how that duct tape gets there by needing to apply quite a lot of it ourselves. 

## Whats next for AutoResumed?
I think for this project to go forward it requires a lot of reimagining and refactoring. The CLI will be fleshed out (as right now it exists as more or less a string parser). Its really exploded in a lot of different areas and being able to structure this and set it up with nix flakes to both instance a server and install dependancies for the comand line tool would be an amazing feat turning this from a hacked together website to a flexable peice of equipment. 
