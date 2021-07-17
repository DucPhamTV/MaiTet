// frontend/src/components/items/AddItem.js
import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import { addItem } from "./ItemsActions";

class AddItem extends Component {
  constructor(props) {
    super(props);
    this.state = {
      description: "",
      url: "",
      target: "",
    };
  }
  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onAddClick = () => {
    const item = {
      description: this.state.description,
      url: this.state.url,
      target: this.state.target,
    };
    this.props.addItem(item);
  };

  render() {
    return (
      <div>
        <h2>Add new Item</h2>
        <Form>
          <Form.Group controlId="contentId">
            <Form.Label>Item</Form.Label>
            <Form.Control
              as="textarea"
              rows={3}
              name="description"
              placeholder="Enter description"
              value={this.name}
              onChange={this.onChange}
            />
            <Form.Control
              as="textarea"
              rows={3}
              name="url"
              placeholder="Enter URL"
              value={this.description}
              onChange={this.onChange}
            />
            <Form.Control
              as="textarea"
              rows={3}
              name="target"
              placeholder="Enter target"
              value={this.content}
              onChange={this.onChange}
            />
          </Form.Group>
        </Form>
        <Button variant="success" onClick={this.onAddClick}>
          Add Item
        </Button>
      </div>
    );
  }
}

AddItem.propTypes = {
  addItem: PropTypes.func.isRequired
};

const mapStateToProps = state => ({});

export default connect(mapStateToProps, { addItem })(withRouter(AddItem));
