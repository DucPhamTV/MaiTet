import React, { Component } from "react";
import PropTypes from "prop-types";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { deleteItem, updateItem } from "./ItemsActions";
import { Button } from "react-bootstrap";

class Item extends Component {
    onDeleteClick = () => {
        const { item } = this.props;
        this.props.deleteItem(item.uuid);
    };
    onIncreasePrice = () => {
        const { item } = this.props;
        item.price += 1000000;
        this.props.updateItem(item.uuid, item);
    };
    render() {
        const { item } = this.props;
        return (
            <>
                <div>
                    <p>{item.name}</p>
                </div>
                <Button variant="danger" size="sm" onClick={this.onDeleteClick}>
                    Delete
                </Button>
                <Button variant="info" size="sm" onClick={this.onIncreasePrice}>
                    Increase price
                </Button>
            </>
        );
    }
}

Item.propTypes = {
    item: PropTypes.object.isRequired
};
const mapStateToProps = state => ({});
export default connect(mapStateToProps, { deleteItem, updateItem })(
    withRouter(Item),
);
