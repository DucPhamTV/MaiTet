import React, { Component } from "react";
import PropTypes from "prop-types";

class Item extends Component {
    render() {
        const { item } = this.props;
        return (
            <div>
                <p>{item.name}</p>
            </div>
        );
    }
}

Item.PropTypes = {
    item: PropTypes.object.isRequired
};
export default Item;