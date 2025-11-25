---
description: 
globs: 
alwaysApply: false
---
# Odoo Naming Conventions

# Naming Conventions for Odoo 17 Custom Modules with "novus" Prefix

## 1. Module Naming
- All custom modules must be prefixed with `novus_`.
- **Examples**:
  - `novus_sales`
  - `novus_project`
  - `novus_abc_report`

## 2. Custom Models
- **File Naming**: Use `novus_<module_name>_<model_name>.py`.
  - **Example**: `models/novus_sales_custom_model.py`
- **Class Naming**: Use camelcase with "Novus" prefix.
  - **Example**: `class NovusSalesCustomModel(models.Model)`
- **Technical Name**: Use `_name = 'novus.<module_name>.<model_name>'`.
  - **Example**: `_name = 'novus.sales.custom_model'`
- **XML ID**: Prefix with `novus.<module_name>.model.`.
  - **Example**: `id="novus.sales.model.custom_model"`

## 3. Inherited Models
- **File Naming**: Use the original model name within your module.
  - **Example**: `models/res_partner.py` in `novus_sales`
- **Class Naming**: Same as original model.
  - **Example**: `class ResPartner(models.Model): _inherit = 'res.partner'`
- **Technical Name**: No change; use original name.
  - **Example**: `_inherit = 'res.partner'`

## 4. Views
- **Custom Views**:
  - **File Naming**: `novus_<module_name>_<model_name>_views.xml`
    - **Example**: `views/novus_sales_custom_model_views.xml`
  - **XML ID**: `novus.<module_name>.view.<view_type>.<model_name>`
    - **Example**: `id="novus.sales.view.form.custom_model"`
- **Inherited Views**:
  - **File Naming**: Include in `novus_<module_name>_views.xml` or separate files.
    - **Example**: `views/novus_sales_views.xml`
  - **XML ID**: `novus_<module_name>_view_<original_model>_<view_type>`
    - **Example**: `id="novus_sales_view_users_form"`
  - **Name Field**: `<original_model>.<view_type>.inherit.novus_<module_name>`
    - **Example**: `name="res.users.form.inherit.novus_sales"`
  - **Example**:
    ```xml
    <record id="novus_sales_view_users_form" model="ir.ui.view">
        <field name="name">res.users.form.inherit.novus_sales</field>
        <field name="model">res.users</field>
        <field name="inherit_id" ref="base.view_users_form"/>
        <field name="arch" type="xml">
            <xpath expr="//label[@for='login']" position="replace">
                <label for="login" string="Login ID / Email Address"/>
            </xpath>
            <xpath expr="//field[@name='login']" position="after">
                <field name="email"/>
            </xpath>
        </field>
    </record>
    ```

## 5. Other XML IDs
- **Menus**: `novus.<module_name>.menu.<menu_name>`
  - **Example**: `id="novus.sales.menu.custom_menu"`
- **Actions**: `novus.<module_name>.action.<action_name>`
  - **Example**: `id="novus.sales.action.custom_action"`
- **Groups**: `novus.<module_name>.group.<group_name>`
  - **Example**: `id="novus.sales.group.custom_group"`
- **Rules**: `novus.<module_name>.rule.<rule_name>`
  - **Example**: `id="novus.sales.rule.custom_rule"`

## 6. Additional Guidelines
- Follow [Odoo 17 Coding Guidelines](https://www.odoo.com/documentation/17.0/th/contributing/development/coding_guidelines.html).
- Ensure file permissions: folders 755, files 644.
- Use `novus` prefix to avoid conflicts with standard Odoo or third-party modules.

 

## 7. Rule to enforce naming conventions
This rule enforces naming conventions for Odoo models and files in the project.
 
## Model Name Convention
- **Description**: Model names must follow Odoo 17 guidelines and start with 'novus'
- **Pattern**: `_name\s*=\s*['"]([^'"]+)['"]`
- **Message**: Model name '${1}' must start with 'novus' and follow Odoo naming convention (module.model format)
- **Severity**: error
- **File Pattern**: `custom_addons/**/*.py`
- **Not Match**: `^novus\.`
 
## File Name Convention
- **Description**: File names for models must start with 'novus_'
- **Pattern**: `class\s+([A-Za-z][A-Za-z0-9_]*)\s*\(\s*models\.Model`
- **Message**: File containing model '${1}' must be named with prefix 'novus_'
- **Severity**: error
- **File Pattern**: `custom_addons/**/*.py`
- **Not Match**: `novus_`
 
