# This file was generated by the "yardl" tool. DO NOT EDIT.

# pyright: reportUnusedClass=false
# pyright: reportUnusedImport=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false

import collections.abc
import io
import typing

import numpy as np
import numpy.typing as npt

from .types import *
from .protocols import *
from . import _ndjson
from . import yardl_types as yardl

class _CoincidenceEventConverter(_ndjson.JsonConverter[CoincidenceEvent, np.void]):
    def __init__(self) -> None:
        self._detector_1_id_converter = _ndjson.uint32_converter
        self._detector_2_id_converter = _ndjson.uint32_converter
        self._tof_idx_converter = _ndjson.uint32_converter
        self._energy_1_idx_converter = _ndjson.uint32_converter
        self._energy_2_idx_converter = _ndjson.uint32_converter
        super().__init__(np.dtype([
            ("detector_1_id", self._detector_1_id_converter.overall_dtype()),
            ("detector_2_id", self._detector_2_id_converter.overall_dtype()),
            ("tof_idx", self._tof_idx_converter.overall_dtype()),
            ("energy_1_idx", self._energy_1_idx_converter.overall_dtype()),
            ("energy_2_idx", self._energy_2_idx_converter.overall_dtype()),
        ]))

    def to_json(self, value: CoincidenceEvent) -> object:
        if not isinstance(value, CoincidenceEvent): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'CoincidenceEvent' instance")
        json_object = {}

        json_object["detector1Id"] = self._detector_1_id_converter.to_json(value.detector_1_id)
        json_object["detector2Id"] = self._detector_2_id_converter.to_json(value.detector_2_id)
        json_object["tofIdx"] = self._tof_idx_converter.to_json(value.tof_idx)
        json_object["energy1Idx"] = self._energy_1_idx_converter.to_json(value.energy_1_idx)
        json_object["energy2Idx"] = self._energy_2_idx_converter.to_json(value.energy_2_idx)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["detector1Id"] = self._detector_1_id_converter.numpy_to_json(value["detector_1_id"])
        json_object["detector2Id"] = self._detector_2_id_converter.numpy_to_json(value["detector_2_id"])
        json_object["tofIdx"] = self._tof_idx_converter.numpy_to_json(value["tof_idx"])
        json_object["energy1Idx"] = self._energy_1_idx_converter.numpy_to_json(value["energy_1_idx"])
        json_object["energy2Idx"] = self._energy_2_idx_converter.numpy_to_json(value["energy_2_idx"])
        return json_object

    def from_json(self, json_object: object) -> CoincidenceEvent:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return CoincidenceEvent(
            detector_1_id=self._detector_1_id_converter.from_json(json_object["detector1Id"],),
            detector_2_id=self._detector_2_id_converter.from_json(json_object["detector2Id"],),
            tof_idx=self._tof_idx_converter.from_json(json_object["tofIdx"],),
            energy_1_idx=self._energy_1_idx_converter.from_json(json_object["energy1Idx"],),
            energy_2_idx=self._energy_2_idx_converter.from_json(json_object["energy2Idx"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._detector_1_id_converter.from_json_to_numpy(json_object["detector1Id"]),
            self._detector_2_id_converter.from_json_to_numpy(json_object["detector2Id"]),
            self._tof_idx_converter.from_json_to_numpy(json_object["tofIdx"]),
            self._energy_1_idx_converter.from_json_to_numpy(json_object["energy1Idx"]),
            self._energy_2_idx_converter.from_json_to_numpy(json_object["energy2Idx"]),
        ) # type:ignore 


class _SubjectConverter(_ndjson.JsonConverter[Subject, np.void]):
    def __init__(self) -> None:
        self._name_converter = _ndjson.OptionalConverter(_ndjson.string_converter)
        self._id_converter = _ndjson.string_converter
        super().__init__(np.dtype([
            ("name", self._name_converter.overall_dtype()),
            ("id", self._id_converter.overall_dtype()),
        ]))

    def to_json(self, value: Subject) -> object:
        if not isinstance(value, Subject): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'Subject' instance")
        json_object = {}

        if value.name is not None:
            json_object["name"] = self._name_converter.to_json(value.name)
        json_object["id"] = self._id_converter.to_json(value.id)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        if (field_val := value["name"]) is not None:
            json_object["name"] = self._name_converter.numpy_to_json(field_val)
        json_object["id"] = self._id_converter.numpy_to_json(value["id"])
        return json_object

    def from_json(self, json_object: object) -> Subject:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return Subject(
            name=self._name_converter.from_json(json_object.get("name")),
            id=self._id_converter.from_json(json_object["id"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._name_converter.from_json_to_numpy(json_object.get("name")),
            self._id_converter.from_json_to_numpy(json_object["id"]),
        ) # type:ignore 


class _InstitutionConverter(_ndjson.JsonConverter[Institution, np.void]):
    def __init__(self) -> None:
        self._name_converter = _ndjson.string_converter
        self._address_converter = _ndjson.string_converter
        super().__init__(np.dtype([
            ("name", self._name_converter.overall_dtype()),
            ("address", self._address_converter.overall_dtype()),
        ]))

    def to_json(self, value: Institution) -> object:
        if not isinstance(value, Institution): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'Institution' instance")
        json_object = {}

        json_object["name"] = self._name_converter.to_json(value.name)
        json_object["address"] = self._address_converter.to_json(value.address)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["name"] = self._name_converter.numpy_to_json(value["name"])
        json_object["address"] = self._address_converter.numpy_to_json(value["address"])
        return json_object

    def from_json(self, json_object: object) -> Institution:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return Institution(
            name=self._name_converter.from_json(json_object["name"],),
            address=self._address_converter.from_json(json_object["address"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._name_converter.from_json_to_numpy(json_object["name"]),
            self._address_converter.from_json_to_numpy(json_object["address"]),
        ) # type:ignore 


class _ExamInformationConverter(_ndjson.JsonConverter[ExamInformation, np.void]):
    def __init__(self) -> None:
        self._subject_converter = _SubjectConverter()
        self._institution_converter = _InstitutionConverter()
        self._protocol_converter = _ndjson.OptionalConverter(_ndjson.string_converter)
        self._start_of_acquisition_converter = _ndjson.OptionalConverter(_ndjson.datetime_converter)
        super().__init__(np.dtype([
            ("subject", self._subject_converter.overall_dtype()),
            ("institution", self._institution_converter.overall_dtype()),
            ("protocol", self._protocol_converter.overall_dtype()),
            ("start_of_acquisition", self._start_of_acquisition_converter.overall_dtype()),
        ]))

    def to_json(self, value: ExamInformation) -> object:
        if not isinstance(value, ExamInformation): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'ExamInformation' instance")
        json_object = {}

        json_object["subject"] = self._subject_converter.to_json(value.subject)
        json_object["institution"] = self._institution_converter.to_json(value.institution)
        if value.protocol is not None:
            json_object["protocol"] = self._protocol_converter.to_json(value.protocol)
        if value.start_of_acquisition is not None:
            json_object["startOfAcquisition"] = self._start_of_acquisition_converter.to_json(value.start_of_acquisition)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["subject"] = self._subject_converter.numpy_to_json(value["subject"])
        json_object["institution"] = self._institution_converter.numpy_to_json(value["institution"])
        if (field_val := value["protocol"]) is not None:
            json_object["protocol"] = self._protocol_converter.numpy_to_json(field_val)
        if (field_val := value["start_of_acquisition"]) is not None:
            json_object["startOfAcquisition"] = self._start_of_acquisition_converter.numpy_to_json(field_val)
        return json_object

    def from_json(self, json_object: object) -> ExamInformation:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return ExamInformation(
            subject=self._subject_converter.from_json(json_object["subject"],),
            institution=self._institution_converter.from_json(json_object["institution"],),
            protocol=self._protocol_converter.from_json(json_object.get("protocol")),
            start_of_acquisition=self._start_of_acquisition_converter.from_json(json_object.get("startOfAcquisition")),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._subject_converter.from_json_to_numpy(json_object["subject"]),
            self._institution_converter.from_json_to_numpy(json_object["institution"]),
            self._protocol_converter.from_json_to_numpy(json_object.get("protocol")),
            self._start_of_acquisition_converter.from_json_to_numpy(json_object.get("startOfAcquisition")),
        ) # type:ignore 


class _DetectorConverter(_ndjson.JsonConverter[Detector, np.void]):
    def __init__(self) -> None:
        self._id_converter = _ndjson.uint32_converter
        self._x_converter = _ndjson.float32_converter
        self._y_converter = _ndjson.float32_converter
        self._z_converter = _ndjson.float32_converter
        super().__init__(np.dtype([
            ("id", self._id_converter.overall_dtype()),
            ("x", self._x_converter.overall_dtype()),
            ("y", self._y_converter.overall_dtype()),
            ("z", self._z_converter.overall_dtype()),
        ]))

    def to_json(self, value: Detector) -> object:
        if not isinstance(value, Detector): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'Detector' instance")
        json_object = {}

        json_object["id"] = self._id_converter.to_json(value.id)
        json_object["x"] = self._x_converter.to_json(value.x)
        json_object["y"] = self._y_converter.to_json(value.y)
        json_object["z"] = self._z_converter.to_json(value.z)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["id"] = self._id_converter.numpy_to_json(value["id"])
        json_object["x"] = self._x_converter.numpy_to_json(value["x"])
        json_object["y"] = self._y_converter.numpy_to_json(value["y"])
        json_object["z"] = self._z_converter.numpy_to_json(value["z"])
        return json_object

    def from_json(self, json_object: object) -> Detector:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return Detector(
            id=self._id_converter.from_json(json_object["id"],),
            x=self._x_converter.from_json(json_object["x"],),
            y=self._y_converter.from_json(json_object["y"],),
            z=self._z_converter.from_json(json_object["z"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._id_converter.from_json_to_numpy(json_object["id"]),
            self._x_converter.from_json_to_numpy(json_object["x"]),
            self._y_converter.from_json_to_numpy(json_object["y"]),
            self._z_converter.from_json_to_numpy(json_object["z"]),
        ) # type:ignore 


class _ScannerInformationConverter(_ndjson.JsonConverter[ScannerInformation, np.void]):
    def __init__(self) -> None:
        self._model_name_converter = _ndjson.OptionalConverter(_ndjson.string_converter)
        self._detectors_converter = _ndjson.VectorConverter(_DetectorConverter())
        self._tof_bin_edges_converter = _ndjson.NDArrayConverter(_ndjson.float32_converter, 1)
        self._tof_resolution_converter = _ndjson.float32_converter
        self._energy_bin_edges_converter = _ndjson.NDArrayConverter(_ndjson.float32_converter, 1)
        self._energy_resolution_at_511_converter = _ndjson.float32_converter
        self._listmode_time_block_duration_converter = _ndjson.uint32_converter
        super().__init__(np.dtype([
            ("model_name", self._model_name_converter.overall_dtype()),
            ("detectors", self._detectors_converter.overall_dtype()),
            ("tof_bin_edges", self._tof_bin_edges_converter.overall_dtype()),
            ("tof_resolution", self._tof_resolution_converter.overall_dtype()),
            ("energy_bin_edges", self._energy_bin_edges_converter.overall_dtype()),
            ("energy_resolution_at_511", self._energy_resolution_at_511_converter.overall_dtype()),
            ("listmode_time_block_duration", self._listmode_time_block_duration_converter.overall_dtype()),
        ]))

    def to_json(self, value: ScannerInformation) -> object:
        if not isinstance(value, ScannerInformation): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'ScannerInformation' instance")
        json_object = {}

        if value.model_name is not None:
            json_object["modelName"] = self._model_name_converter.to_json(value.model_name)
        json_object["detectors"] = self._detectors_converter.to_json(value.detectors)
        json_object["tofBinEdges"] = self._tof_bin_edges_converter.to_json(value.tof_bin_edges)
        json_object["tofResolution"] = self._tof_resolution_converter.to_json(value.tof_resolution)
        json_object["energyBinEdges"] = self._energy_bin_edges_converter.to_json(value.energy_bin_edges)
        json_object["energyResolutionAt511"] = self._energy_resolution_at_511_converter.to_json(value.energy_resolution_at_511)
        json_object["listmodeTimeBlockDuration"] = self._listmode_time_block_duration_converter.to_json(value.listmode_time_block_duration)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        if (field_val := value["model_name"]) is not None:
            json_object["modelName"] = self._model_name_converter.numpy_to_json(field_val)
        json_object["detectors"] = self._detectors_converter.numpy_to_json(value["detectors"])
        json_object["tofBinEdges"] = self._tof_bin_edges_converter.numpy_to_json(value["tof_bin_edges"])
        json_object["tofResolution"] = self._tof_resolution_converter.numpy_to_json(value["tof_resolution"])
        json_object["energyBinEdges"] = self._energy_bin_edges_converter.numpy_to_json(value["energy_bin_edges"])
        json_object["energyResolutionAt511"] = self._energy_resolution_at_511_converter.numpy_to_json(value["energy_resolution_at_511"])
        json_object["listmodeTimeBlockDuration"] = self._listmode_time_block_duration_converter.numpy_to_json(value["listmode_time_block_duration"])
        return json_object

    def from_json(self, json_object: object) -> ScannerInformation:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return ScannerInformation(
            model_name=self._model_name_converter.from_json(json_object.get("modelName")),
            detectors=self._detectors_converter.from_json(json_object["detectors"],),
            tof_bin_edges=self._tof_bin_edges_converter.from_json(json_object["tofBinEdges"],),
            tof_resolution=self._tof_resolution_converter.from_json(json_object["tofResolution"],),
            energy_bin_edges=self._energy_bin_edges_converter.from_json(json_object["energyBinEdges"],),
            energy_resolution_at_511=self._energy_resolution_at_511_converter.from_json(json_object["energyResolutionAt511"],),
            listmode_time_block_duration=self._listmode_time_block_duration_converter.from_json(json_object["listmodeTimeBlockDuration"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._model_name_converter.from_json_to_numpy(json_object.get("modelName")),
            self._detectors_converter.from_json_to_numpy(json_object["detectors"]),
            self._tof_bin_edges_converter.from_json_to_numpy(json_object["tofBinEdges"]),
            self._tof_resolution_converter.from_json_to_numpy(json_object["tofResolution"]),
            self._energy_bin_edges_converter.from_json_to_numpy(json_object["energyBinEdges"]),
            self._energy_resolution_at_511_converter.from_json_to_numpy(json_object["energyResolutionAt511"]),
            self._listmode_time_block_duration_converter.from_json_to_numpy(json_object["listmodeTimeBlockDuration"]),
        ) # type:ignore 


class _HeaderConverter(_ndjson.JsonConverter[Header, np.void]):
    def __init__(self) -> None:
        self._scanner_converter = _ScannerInformationConverter()
        self._exam_converter = _ndjson.OptionalConverter(_ExamInformationConverter())
        super().__init__(np.dtype([
            ("scanner", self._scanner_converter.overall_dtype()),
            ("exam", self._exam_converter.overall_dtype()),
        ]))

    def to_json(self, value: Header) -> object:
        if not isinstance(value, Header): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'Header' instance")
        json_object = {}

        json_object["scanner"] = self._scanner_converter.to_json(value.scanner)
        if value.exam is not None:
            json_object["exam"] = self._exam_converter.to_json(value.exam)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["scanner"] = self._scanner_converter.numpy_to_json(value["scanner"])
        if (field_val := value["exam"]) is not None:
            json_object["exam"] = self._exam_converter.numpy_to_json(field_val)
        return json_object

    def from_json(self, json_object: object) -> Header:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return Header(
            scanner=self._scanner_converter.from_json(json_object["scanner"],),
            exam=self._exam_converter.from_json(json_object.get("exam")),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._scanner_converter.from_json_to_numpy(json_object["scanner"]),
            self._exam_converter.from_json_to_numpy(json_object.get("exam")),
        ) # type:ignore 


class _TimeBlockConverter(_ndjson.JsonConverter[TimeBlock, np.void]):
    def __init__(self) -> None:
        self._id_converter = _ndjson.uint32_converter
        self._prompt_events_converter = _ndjson.VectorConverter(_CoincidenceEventConverter())
        self._delayed_events_converter = _ndjson.OptionalConverter(_ndjson.VectorConverter(_CoincidenceEventConverter()))
        super().__init__(np.dtype([
            ("id", self._id_converter.overall_dtype()),
            ("prompt_events", self._prompt_events_converter.overall_dtype()),
            ("delayed_events", self._delayed_events_converter.overall_dtype()),
        ]))

    def to_json(self, value: TimeBlock) -> object:
        if not isinstance(value, TimeBlock): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'TimeBlock' instance")
        json_object = {}

        json_object["id"] = self._id_converter.to_json(value.id)
        json_object["promptEvents"] = self._prompt_events_converter.to_json(value.prompt_events)
        if value.delayed_events is not None:
            json_object["delayedEvents"] = self._delayed_events_converter.to_json(value.delayed_events)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["id"] = self._id_converter.numpy_to_json(value["id"])
        json_object["promptEvents"] = self._prompt_events_converter.numpy_to_json(value["prompt_events"])
        if (field_val := value["delayed_events"]) is not None:
            json_object["delayedEvents"] = self._delayed_events_converter.numpy_to_json(field_val)
        return json_object

    def from_json(self, json_object: object) -> TimeBlock:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return TimeBlock(
            id=self._id_converter.from_json(json_object["id"],),
            prompt_events=self._prompt_events_converter.from_json(json_object["promptEvents"],),
            delayed_events=self._delayed_events_converter.from_json(json_object.get("delayedEvents")),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._id_converter.from_json_to_numpy(json_object["id"]),
            self._prompt_events_converter.from_json_to_numpy(json_object["promptEvents"]),
            self._delayed_events_converter.from_json_to_numpy(json_object.get("delayedEvents")),
        ) # type:ignore 


class _TimeIntervalConverter(_ndjson.JsonConverter[TimeInterval, np.void]):
    def __init__(self) -> None:
        self._start_converter = _ndjson.uint32_converter
        self._stop_converter = _ndjson.uint32_converter
        super().__init__(np.dtype([
            ("start", self._start_converter.overall_dtype()),
            ("stop", self._stop_converter.overall_dtype()),
        ]))

    def to_json(self, value: TimeInterval) -> object:
        if not isinstance(value, TimeInterval): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'TimeInterval' instance")
        json_object = {}

        json_object["start"] = self._start_converter.to_json(value.start)
        json_object["stop"] = self._stop_converter.to_json(value.stop)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["start"] = self._start_converter.numpy_to_json(value["start"])
        json_object["stop"] = self._stop_converter.numpy_to_json(value["stop"])
        return json_object

    def from_json(self, json_object: object) -> TimeInterval:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return TimeInterval(
            start=self._start_converter.from_json(json_object["start"],),
            stop=self._stop_converter.from_json(json_object["stop"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._start_converter.from_json_to_numpy(json_object["start"]),
            self._stop_converter.from_json_to_numpy(json_object["stop"]),
        ) # type:ignore 


class _TimeFrameInformationConverter(_ndjson.JsonConverter[TimeFrameInformation, np.void]):
    def __init__(self) -> None:
        self._time_frames_converter = _ndjson.VectorConverter(_TimeIntervalConverter())
        super().__init__(np.dtype([
            ("time_frames", self._time_frames_converter.overall_dtype()),
        ]))

    def to_json(self, value: TimeFrameInformation) -> object:
        if not isinstance(value, TimeFrameInformation): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'TimeFrameInformation' instance")
        json_object = {}

        json_object["timeFrames"] = self._time_frames_converter.to_json(value.time_frames)
        return json_object

    def numpy_to_json(self, value: np.void) -> object:
        if not isinstance(value, np.void): # pyright: ignore [reportUnnecessaryIsInstance]
            raise TypeError("Expected 'np.void' instance")
        json_object = {}

        json_object["timeFrames"] = self._time_frames_converter.numpy_to_json(value["time_frames"])
        return json_object

    def from_json(self, json_object: object) -> TimeFrameInformation:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return TimeFrameInformation(
            time_frames=self._time_frames_converter.from_json(json_object["timeFrames"],),
        )

    def from_json_to_numpy(self, json_object: object) -> np.void:
        if not isinstance(json_object, dict):
            raise TypeError("Expected 'dict' instance")
        return (
            self._time_frames_converter.from_json_to_numpy(json_object["timeFrames"]),
        ) # type:ignore 


class NDJsonPrdExperimentWriter(_ndjson.NDJsonProtocolWriter, PrdExperimentWriterBase):
    """NDJson writer for the PrdExperiment protocol."""


    def __init__(self, stream: typing.Union[typing.TextIO, str]) -> None:
        PrdExperimentWriterBase.__init__(self)
        _ndjson.NDJsonProtocolWriter.__init__(self, stream, PrdExperimentWriterBase.schema)

    def _write_header(self, value: Header) -> None:
        converter = _HeaderConverter()
        json_value = converter.to_json(value)
        self._write_json_line({"header": json_value})

    def _write_time_blocks(self, value: collections.abc.Iterable[TimeBlock]) -> None:
        converter = _TimeBlockConverter()
        for item in value:
            json_item = converter.to_json(item)
            self._write_json_line({"timeBlocks": json_item})


class NDJsonPrdExperimentReader(_ndjson.NDJsonProtocolReader, PrdExperimentReaderBase):
    """NDJson writer for the PrdExperiment protocol."""


    def __init__(self, stream: typing.Union[io.BufferedReader, typing.TextIO, str]) -> None:
        PrdExperimentReaderBase.__init__(self)
        _ndjson.NDJsonProtocolReader.__init__(self, stream, PrdExperimentReaderBase.schema)

    def _read_header(self) -> Header:
        json_object = self._read_json_line("header", True)
        converter = _HeaderConverter()
        return converter.from_json(json_object)

    def _read_time_blocks(self) -> collections.abc.Iterable[TimeBlock]:
        converter = _TimeBlockConverter()
        while (json_object := self._read_json_line("timeBlocks", False)) is not _ndjson.MISSING_SENTINEL:
            yield converter.from_json(json_object)

