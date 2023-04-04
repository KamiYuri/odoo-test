/** @odoo-module **/

import {registry} from "@web/core/registry";
import {Layout} from "@web/search/layout";

const {Component, useState, xml} = owl;

class ModuleAWelcome extends Component {
  redirect_func() {
    alert('hihi');
  }
}

ModuleAWelcome.components = {Layout};
ModuleAWelcome.template = 'module_a.client_action';

registry.category("lazy_components").add("ModuleAWelcome", ModuleAWelcome);
