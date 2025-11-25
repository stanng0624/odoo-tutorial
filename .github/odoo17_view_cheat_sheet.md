# Odoo 17.0 View Attributes Cheat Sheet

## ❌ Deprecated Syntax (Do Not Use)

```xml
<!-- Avoid using attrs attribute -->
<field name="partner_id" attrs="{'invisible': [('has_partner', '=', False)]}"/>

<!-- Avoid using states attribute -->
<field name="notes" states="{'readonly': [('state', 'not in', ['draft'])]}"/>
```

## ✅ New Syntax in Odoo 17.0

### Visibility Control

```xml
<!-- Instead of attrs="{'invisible': [('field', '=', value)]}" -->
<field name="partner_id" invisible="field == value"/>
<field name="amount" invisible="not is_paid"/>
<field name="notes" invisible="state not in ['draft', 'pending']"/>
```

### Read-only Control

```xml
<!-- Instead of attrs="{'readonly': [('field', '=', value)]}" -->
<field name="partner_id" readonly="field == value"/>
<field name="amount" readonly="state != 'draft'"/>
<field name="notes" readonly="is_confirmed or is_canceled"/>
```

### Required Control

```xml
<!-- Instead of attrs="{'required': [('field', '=', value)]}" -->
<field name="partner_id" required="field == value"/>
<field name="amount" required="payment_type == 'inbound'"/>
<field name="notes" required="require_notes"/>
```

### Common Operators

| Old Domain | New Expression |
|------------|---------------|
| `('field', '=', value)` | `field == value` |
| `('field', '!=', value)` | `field != value` |
| `('field', 'in', [values])` | `field in [values]` |
| `('field', 'not in', [values])` | `field not in [values]` |
| `('field', '>', value)` | `field > value` |
| `('field', '<', value)` | `field < value` |
| `('field', '>=', value)` | `field >= value` |
| `('field', '<=', value)` | `field <= value` |
| `('field', '=', True)` | `field` or `field == True` |
| `('field', '=', False)` | `not field` or `field == False` |
| `'&', A, B` | `A and B` |
| `'|', A, B` | `A or B` |
| `'!', A` | `not A` |

### Complex Expressions

```xml
<!-- AND condition -->
<field name="shipping_note" invisible="not international and not is_large"/>

<!-- OR condition -->
<field name="account_number" invisible="payment_type != 'bank' or is_internal"/>

<!-- Parentheses for grouping -->
<field name="tax_id" invisible="(is_free or amount == 0) and not force_tax"/>
```

### Button Controls

```xml
<button name="action_confirm" string="Confirm" 
        invisible="state != 'draft'"
        readonly="not is_allowed"/>
```

### Group and Section Controls

```xml
<group string="Shipping Details" invisible="delivery_type == 'digital'">
    <!-- Fields related to shipping -->
</group>

<notebook invisible="is_simple_view">
    <page string="Advanced" invisible="user_type == 'basic'">
        <!-- Advanced fields -->
    </page>
</notebook>
```

### Tree View Column Visibility

```xml
<field name="tax_id" column_invisible="context.get('hide_tax')"/>
```

## 🔍 Find Deprecated Attrs

Run this command to check your codebase for deprecated attributes:

```bash
python3 /Users/Workspace/Development/workspace/odoo/novus-odoo/silverlit-odoo17/docs/check_views_for_attrs.py /path/to/module
``` 