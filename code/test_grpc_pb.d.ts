import * as jspb from 'google-protobuf'



export class testRequest extends jspb.Message {
  getIter(): number;
  setIter(value: number): testRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): testRequest.AsObject;
  static toObject(includeInstance: boolean, msg: testRequest): testRequest.AsObject;
  static serializeBinaryToWriter(message: testRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): testRequest;
  static deserializeBinaryFromReader(message: testRequest, reader: jspb.BinaryReader): testRequest;
}

export namespace testRequest {
  export type AsObject = {
    iter: number,
  }
}

export class testStreamRequest extends jspb.Message {
  getIter(): number;
  setIter(value: number): testStreamRequest;

  getBatchnum(): number;
  setBatchnum(value: number): testStreamRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): testStreamRequest.AsObject;
  static toObject(includeInstance: boolean, msg: testStreamRequest): testStreamRequest.AsObject;
  static serializeBinaryToWriter(message: testStreamRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): testStreamRequest;
  static deserializeBinaryFromReader(message: testStreamRequest, reader: jspb.BinaryReader): testStreamRequest;
}

export namespace testStreamRequest {
  export type AsObject = {
    iter: number,
    batchnum: number,
  }
}

export class testResponse extends jspb.Message {
  getResList(): Array<testType>;
  setResList(value: Array<testType>): testResponse;
  clearResList(): testResponse;
  addRes(value?: testType, index?: number): testType;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): testResponse.AsObject;
  static toObject(includeInstance: boolean, msg: testResponse): testResponse.AsObject;
  static serializeBinaryToWriter(message: testResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): testResponse;
  static deserializeBinaryFromReader(message: testResponse, reader: jspb.BinaryReader): testResponse;
}

export namespace testResponse {
  export type AsObject = {
    resList: Array<testType.AsObject>,
  }
}

export class testType extends jspb.Message {
  getMattype(): string;
  setMattype(value: string): testType;

  getFabname(): string;
  setFabname(value: string): testType;

  getChmbrendperiod(): number;
  setChmbrendperiod(value: number): testType;

  getMatno(): string;
  setMatno(value: string): testType;

  getIndname(): string;
  setIndname(value: string): testType;

  getWaferid(): string;
  setWaferid(value: string): testType;

  getCntxid(): string;
  setCntxid(value: string): testType;

  getUsageval(): number;
  setUsageval(value: number): testType;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): testType.AsObject;
  static toObject(includeInstance: boolean, msg: testType): testType.AsObject;
  static serializeBinaryToWriter(message: testType, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): testType;
  static deserializeBinaryFromReader(message: testType, reader: jspb.BinaryReader): testType;
}

export namespace testType {
  export type AsObject = {
    mattype: string,
    fabname: string,
    chmbrendperiod: number,
    matno: string,
    indname: string,
    waferid: string,
    cntxid: string,
    usageval: number,
  }
}

