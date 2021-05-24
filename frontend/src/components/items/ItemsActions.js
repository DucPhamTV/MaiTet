import axios from "axios";
import { toastOnError } from "../../utils/Utils";
import { GET_ITEMS, ADD_ITEM, DELETE_ITEM, UPDATE_ITEM } from "./ItemsTypes";

export const getItems = () => dispatch => {
    axios
        .get("/v1/items/")
        .then(response => {
	    console.log(response);
            dispatch({
                type: GET_ITEMS,
                payload: response.data.results,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};

export const addItem = item => dispatch => {
    axios
        .post("v1/items/", item)
        .then(response => {
            dispatch({
                type: ADD_ITEM,
                payload: response.data,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};

export const deleteItem = id => dispatch => {
    axios
        .delete(`v1/items/${id}`)
        .then(response => {
            dispatch({
                type: DELETE_ITEM,
                payload: id,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};

export const updateItem = (id, item) => dispatch => {
    axios
        .put(`v1/items/${id}/`, item)
        .then(response => {
            dispatch({
                type: UPDATE_ITEM,
                payload: response.data,
            });
        })
        .catch(error => {
            toastOnError(error);
        });
};

