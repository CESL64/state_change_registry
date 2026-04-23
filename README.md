# State Change Registry

## Overview
`state_change_registry` is the **base module** of the solution. Its purpose is to centralize the registration of state changes for business documents in Odoo 18, serving as the common foundation for invoice, sales, and purchase tracking modules.

This module was designed with a **modular architecture**, allowing each business area to extend the base model independently while keeping the core tracking logic unified and reusable.

## Main Features
- 🧩 Defines the base model `state.change.registry`
- 🕓 Stores the date and time of each change
- 👤 Records the user who executed the transition
- 💰 Saves the total amount at the moment of the change
- 📄 Stores the number of lines and tax snapshot of the original document
- 🏢 Supports company-aware tracking with multi-company rules
- 🔄 Records previous and new states
- ✉️ Includes notification status control through `mail_sent`
- 💬 Adds chatter support for traceability and future communication features
- ⏰ Includes a scheduled action (CRON) to process pending email notifications

## Views and Usability
- `list` view for quick monitoring of state changes
- `form` view in read-only mode for data integrity
- `search` view with:
  - search fields
  - useful filters
  - group by options

## Reports
- 📑 Includes a QWeb report to display the detail of a single state change record
- Uses `web.basic_layout` for a clean and professional output

## Technical Design
This module intentionally **does not depend on a specific business document**.  
Instead, it exposes a reusable base model and a public hook:

- `send_state_change_notification()`

This method is meant to be inherited by dependent modules such as:
- `account_state_change_registry`
- `sale_state_change_registry`
- `purchase_state_change_registry`

That design keeps the base layer clean, extensible, and aligned with good Odoo inheritance practices.

## Dependencies
- `base`
- `mail`

## Functional Goal
This module provides the audit backbone for a broader state-tracking solution in Odoo 18, helping organizations:
- improve traceability
- standardize state transition logs
- support operational control
- prepare the system for automated notifications and reporting
