import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { getItems } from "./ItemsActions";

import Item from "./Item";

class ListItems extends Component {
  componentDidMount() {
    this.props.getItems();
  }

  render() {
    const { items } = this.props.items;

    if (items.length === 0) {
      return <h2>Please add your first item</h2>;
    }

    let items_dom = items.map(item => {
      return <Item key={item.id} item={item} />;
    });

    return (
      <div>
        <h2>Items</h2>
        {items_dom}
      </div>
    );
  }
}

ListItems.propTypes = {
  getItems: PropTypes.func.isRequired,
  items: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  items: state.items
});

export default connect(mapStateToProps, {
  getItems
})(withRouter(ListItems));