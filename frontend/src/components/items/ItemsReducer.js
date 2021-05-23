import { GET_ITEMS, ADD_ITEM } from "./ItemsTypes";

const initialState = {
    items: []
};

export const itemsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ITEMS:
            return {
                ...state,
                items: action.payload,
            };
        case ADD_ITEM:
            return {
                ...state,
                items: [...state.items, action.payload],
            };
        default:
            return state;
    }
};
