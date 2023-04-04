/** @odoo-module */

import { registry } from "@web/core/registry";
import { LazyComponent } from "@web/core/assets";

const { Component, xml } = owl;

class ModuleAWelcomeLoader extends Component {}

ModuleAWelcomeLoader.components = { LazyComponent };
ModuleAWelcomeLoader.template = xml`
<LazyComponent bundle="'module_a.welcome'" Component="'ModuleAWelcome'" props="props"/>
`;

registry.category("actions").add("module_a.welcome", ModuleAWelcomeLoader);
