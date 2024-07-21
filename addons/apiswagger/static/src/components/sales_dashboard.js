/** @odoo-module **/

import { Component } from 'owl';
import { useState } from 'owl/hooks';

class MyOwlComponent extends Component {
    setup() {
        this.state = useState({
            message: "Hello, OWL!",
        });
    }
}

MyOwlComponent.template = 'apiswagger.MyOwlComponent';

export default MyOwlComponent;
