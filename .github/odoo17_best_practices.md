# Odoo 17 Best Practices for Cursor.AI
 
This project follows the Odoo 17 coding guidelines. Please adhere to the following rules when generating code:
 
## General Coding
- Apply Odoo coding guidelines to new modules and developments.
- Maintain the original style for stable version files.
- For master version, apply guidelines to modified code or files under major revision.
 
## Module Structure
- Organize directories as follows: `data/`, `models/`, `controllers/`, `views/`, `static/`, `wizard/`, `report/`, `tests/`.
 
## File Naming
- Models: Split by main model, e.g., `plant_nursery.py`, `plant_order.py`.
- Views: Split by model, suffixed `_views.xml`.
- Data: Split by purpose, e.g., `plant_nursery_data.xml`.
 
## XML Files
- Use `<record>` notation with `id` before `model`.
- Follow naming conventions for menus, views, actions, groups, rules.
- **IMPORTANT**: In Odoo 17, `attrs` and `states` attributes are no longer supported in views.
- Use direct attribute expressions instead of `attrs` and `states`.
- Example conversion:
  ```xml
  <!-- Before (Odoo 16) -->
  <field name="partner_id" attrs="{'invisible': [('has_partner', '=', False)], 'required': [('type', '=', 'sale')]}"/>
  
  <!-- After (Odoo 17) -->
  <field name="partner_id" invisible="has_partner == False" required="type == 'sale'"/>
  ```
- When using the old syntax, you may encounter this error:
  ```
  Since 17.0, the "attrs" and "states" attributes are no longer used.
  ```
 
## Python
- Follow PEP8, ignoring E501, E301, E302.
- Order imports: external libs, odoo, odoo addons, alphabetically.
- Use `with_context` for different contexts.
- Split methods by responsibility; avoid hardcoding logic.
- Use `_()` for translations.
- Method order in classes: private attrs, defaults, fields, computes, onchanges, relateds, inverses, searches, constraints, action methods, business logic, CRUD methods, workspace methods.
 
## JavaScript
- Use `'use strict;'`.
- Use linter (jshint).
- Avoid minified libs.
- Use camelcase for classes.
 
## CSS/SCSS
- Use 4-space indent, max 80 characters per line.
- Order properties from position to decorative.
- Prefix classes with `o_<module_name>`.
 
## View System Changes in Odoo 17
- The `attrs` and `states` attributes are deprecated and no longer supported.
- Use direct attribute expressions for conditional visibility, required fields, etc.
- Use the provided `check_views_for_attrs.py` script to identify views that need updating.
- Follow the examples in the View Guidelines and Cheat Sheet for proper conversion.
 
## Migration Process
1. **Identify Problematic Views:**
   - Run the check views script to scan your codebase:
     ```bash
     python3 check_views_for_attrs.py /path/to/your/module
     ```
   - This will identify all views using the deprecated `attrs` and `states` attributes.
 
2. **Convert Views:**
   - Use the examples in the guidelines and cheat sheet to convert `attrs` to direct attributes.
   - Common conversions:
     - `attrs="{'invisible': [('field', '=', value)]}"` → `invisible="field == value"`
     - `attrs="{'readonly': [('state', 'in', ['done', 'cancel'])]}"` → `readonly="state in ['done', 'cancel']"`
     - `attrs="{'required': [('type', '=', 'sale')]}"` → `required="type == 'sale'"`
 
3. **Test Thoroughly:**
   - After conversion, test all views to ensure they behave as expected.
   - Pay special attention to conditional visibility, required fields, and readonly states.
 
## Additional Practices
- Keep files reasonably sized, focusing on a single responsibility.
- Use descriptive variable and function names.
- Write docstrings for classes and methods.
- Ensure code is testable and write unit tests where applicable.
- When updating views, test thoroughly after conversion from `attrs` to direct attributes.
- Use the official Odoo 17.0 documentation as a reference for view system changes.
 
## Resources
- @Odoo 17.0 View Guidelines
- @View Cheat Sheet
- @Check Views Script
- @Official Odoo 17.0 Documentation