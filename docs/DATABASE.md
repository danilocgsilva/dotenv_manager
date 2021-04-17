# Database

## Explanations for tables

**Table variables**

The variable name that will be stored.

**Table variable_group**

You may require group variables to facilitates the .env file formating. Sometimes, you will require to make a simple line blank separation in the middle of .env file.

**Table environment_group**

The environments that will be used by your projects and group variables

**Table templates**

The projects may require a set o variables. So, at new environment, you will need recreate all same variables.

## Structure

* Table variables
   * id int
   * name string
   * value string
   * variable_group_id (nullable)
   * group_id
   * template_id

* Table variable_group
   * id int

* Table environment_group
    * id int
    * name string

* Table templates
    * id int
    * project_name
