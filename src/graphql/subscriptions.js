/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const onMessage = /* GraphQL */ `
  subscription OnMessage($cciCode: String!, $companyCode: String, $id: String) {
    onMessage(cciCode: $cciCode, companyCode: $companyCode, id: $id) {
      id
      cciCode
      companyCode
      content
      __typename
    }
  }
`;
