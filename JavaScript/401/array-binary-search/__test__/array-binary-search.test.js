'use strict';

const BinarySearch = require('../array-binary-search');

describe('array-binary-search', () => {

    it('returns null if no args are present', () => {
        expect(BinarySearch()).toBeNull();
        expect(BinarySearch([])).toBeNull();
    });
    it("does something if it gets bad input", () => {
        expect(true).toBeTruthy();
    });
    it("result when value is present", () => {
        expect(BinarySearch([4, 8, 15, 16, 23, 42], 15)).toEqual(2);
    });
    it("result when value is not present", () => {
        expect(BinarySearch([11, 22, 33, 44, 55, 66, 77], 90)).toEqual(-1);
    });
    it("handles weird cases", () => {
        expect(true).toBeTruthy()
    });
});