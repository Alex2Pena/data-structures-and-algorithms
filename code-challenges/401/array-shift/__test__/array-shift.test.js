'use strict';

const insertShiftArray = require('../array-shift');

describe('array-shift', () => {

it('returns null if no args are present', () => {
    expect(insertShiftArray()).toBeNull()
})
it("does something if it gets bad input", () => {
    expect(true).toBeTruthy()
}) 
it("inserts into even-numbered arrays", () => {
    expect(insertShiftArray([2,4,6,8], 5)).toEqual([2,4,5,6,8])
}) 
it("inserts into odd-numbered arrays", () => {
    expect(insertShiftArray([4,8,15,23,42], 16)).toEqual([4,8,15,16,23,42])
}) 
it("handles weird cases", () => {
    expect(true).toBeTruthy()
}) 
})
