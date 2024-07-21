/** @odoo-module **/

import { registry } from '@web/core/registry';
import MyOwlComponent from './sales_dashboard.js';

const { ComponentWrapper } = owl;

registry.category('actions').add('my_owl_component', {
    Component: ComponentWrapper(MyOwlComponent),
    props: {},
});
