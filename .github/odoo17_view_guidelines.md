# Odoo 17.0 View Development Guidelines

## Important Changes in Odoo 17.0

Odoo 17.0 introduces significant changes to view definitions that differ from previous versions. This guide will help you avoid common mistakes and ensure compatibility with the new version.

## ⚠️ Deprecated: `attrs` and `states` Attributes

### What Changed?

In Odoo 17.0, the `attrs` and `states` attributes are no longer supported in views. They have been replaced with a simpler, more direct approach using the attributes themselves combined with domain expressions.

### Error Message You Might See

```
Since 17.0, the "attrs" and "states" attributes are no longer used.
```

## ✅ New Approach: Direct Attribute Expressions

### Basic Principles

1. Use the attribute directly (e.g., `invisible`, `readonly`, `required`)
2. Set its value to a domain expression
3. No need for dictionary syntax or wrapping in lists

### Key Attributes to Use Directly

- `invisible` - Controls whether the field is visible
- `readonly` - Controls whether the field is editable
- `required` - Controls whether the field is required
- `column_invisible` - Controls column visibility in tree views

## Examples

### Old Way (Pre-Odoo 17) ❌

```xml
<field name="partner_id" attrs="{'invisible': [('has_partner', '=', False)]}"/>
<field name="amount" attrs="{'readonly': [('state', 'in', ['confirmed', 'done'])]}"/>
<field name="notes" attrs="{'required': [('type', '=', 'detailed')]}"/>
```

### New Way (Odoo 17) ✅

```xml
<field name="partner_id" invisible="has_partner == False"/>
<field name="amount" readonly="state in ['confirmed', 'done']"/>
<field name="notes" required="type == 'detailed'"/>
```

## Domain Expression Syntax

Domain expressions are now written with a simpler Python-like syntax:

| Operation | Old Way | New Way |
|-----------|---------|---------|
| Equality | `[('field', '=', value)]` | `field == value` |
| Inequality | `[('field', '!=', value)]` | `field != value` |
| In list | `[('field', 'in', [values])]` | `field in [values]` |
| Not in list | `[('field', 'not in', [values])]` | `field not in [values]` |
| Greater than | `[('field', '>', value)]` | `field > value` |
| Less than | `[('field', '<', value)]` | `field < value` |
| Greater or equal | `[('field', '>=', value)]` | `field >= value` |
| Less or equal | `[('field', '<=', value)]` | `field <= value` |
| Boolean true | `[('field', '=', True)]` | `field == True` or just `field` |
| Boolean false | `[('field', '=', False)]` | `field == False` or `not field` |

### Complex Expressions

You can combine expressions using:

- `and` instead of AND operator
- `or` instead of OR operator
- Parentheses for grouping

Example:
```xml
<field name="delivery_note" invisible="(state != 'confirmed') or (not has_delivery)"/>
```

## Common Patterns for Group and Div Elements

For containers like `<group>` or `<div>`, you would use:

```xml
<div class="alert alert-warning" invisible="status != 'warning'">
    Warning message here
</div>

<group invisible="type != 'sale'">
    <!-- Sales-specific fields -->
</group>
```

## Working with Buttons

For buttons and actions:

```xml
<!-- Old way -->
<button name="confirm_order" string="Confirm" attrs="{'invisible': [('state', '!=', 'draft')]}"/>

<!-- New way -->
<button name="confirm_order" string="Confirm" invisible="state != 'draft'"/>
```

## Best Practices for View Development in Odoo 17

1. **Test views thoroughly** - After developing a view, test it with different data scenarios
2. **Use proper indentation** - Keep your XML well-formatted for readability
3. **Comment your views** - Add comments for complex visibility logic
4. **Avoid hardcoding IDs** - Use references and external IDs
5. **Group related fields** - Use groups and notebooks to organize your form views
6. **Keep it simple** - Avoid overly complex domain expressions

## Debugging Views

If you encounter view errors:

1. Check the server logs for details about the error
2. Enable developer mode to see more detailed error messages
3. Use the "Edit View" feature in developer mode to make quick changes
4. Remember to export your changes back to the XML files

## Real-World Examples

### Status-based Visibility

```xml
<!-- Show only when document is in draft state -->
<field name="reference" readonly="state != 'draft'"/>

<!-- Hide cancel button if already canceled or done -->
<button name="action_cancel" string="Cancel" invisible="state in ['cancel', 'done']"/>
```

### Type-based Field Requirements

```xml
<!-- Contact name is only required for individual contacts, not companies -->
<field name="contact_name" required="is_company == False"/>

<!-- Company field is required for vendors -->
<field name="company_id" required="partner_type == 'vendor'"/>
```

### Combining Conditions

```xml
<!-- Only visible for draft sales orders with products -->
<button name="confirm_sale" invisible="state != 'draft' or line_ids == []"/>

<!-- Required for international shipments that aren't in the EU -->
<field name="customs_id" required="is_international and not is_eu_country"/>
```

## Handling View Inheritance

When extending existing views, you may need to:

1. Find elements using xpath or field references
2. Add attributes to update behavior
3. Position new elements

Example:

```xml
<record id="view_partner_form_inherited" model="ir.ui.view">
    <field name="name">res.partner.form.inherited</field>
    <field name="model">res.partner</field>
    <field name="inherit_id" ref="base.view_partner_form"/>
    <field name="arch" type="xml">
        <!-- Add readonly attribute to a field -->
        <xpath expr="//field[@name='name']" position="attributes">
            <attribute name="readonly">state == 'done'</attribute>
        </xpath>
        
        <!-- Add a new field after email -->
        <field name="email" position="after">
            <field name="custom_field" invisible="not is_company"/>
        </field>
    </field>
</record>
```

## Migration Checklist

When migrating views from older Odoo versions to Odoo 17:

1. ✅ Replace all instances of `attrs="{...}"` with direct attributes
2. ✅ Replace all instances of `states="{...}"` with direct attributes
3. ✅ Update domain expressions to use the new Python-like syntax
4. ✅ Test all view transitions and states carefully
5. ✅ Review inherited views that might modify attributes

## Additional Resources

- [Official Odoo 17.0 Documentation](https://www.odoo.com/documentation/17.0/developer/reference/frontend/views.html)
- [Odoo 17.0 Upgrade Guide](https://www.odoo.com/documentation/17.0/administration/upgrade.html)
- Internal training materials and examples

## Troubleshooting

If you encounter view errors after migration:

1. Check the server logs for detailed error messages
2. Look for syntax errors in domain expressions
3. Verify field names and model relationships
4. Confirm that all required view elements are present
5. Use the developer tools to inspect view XML and make corrections

## Conclusion

By following these guidelines, you'll avoid common errors and create views that are fully compatible with Odoo 17.0. Remember that the new approach is designed to be more intuitive and maintainable in the long run, despite the initial adjustment period. 