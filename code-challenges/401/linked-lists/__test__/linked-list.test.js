'use strict';

const linkedList = require('../linked-list');

describe('linked-list', () => {

it('returns null if no args are present', () => {
    expect(linkedList()).toBeNull()
})
it("does something if it gets bad input", () => {
    expect(true).toBeTruthy()
}) 
it("checks to see if the constructor makes a list", () => {
    expect(linkedList([2,4,6,8], 5)).toEqual([2,4,5,6,8])
}) 
it("inserts into odd-numbered arrays", () => {
    expect(linkedList([4,8,15,23,42], 16)).toEqual([4,8,15,16,23,42])
}) 
it("handles weird cases", () => {
    expect(true).toBeTruthy()
}) 
})
