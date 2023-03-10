import abc
import torch
import torch.nn as nn
from pytomography.metadata import ObjectMeta, ImageMeta

class CorrectionNet(nn.Module, metaclass=abc.ABCMeta):
    """Correction net is the parent class for all correction networks used in reconstruction. Subclasses must implement the ``forward`` method.

    Args:
        device (str): Pytorch device used for computation
    """
    def __init__(self, device: str = 'cpu') -> None:
        """Used to initialize the correction network.

        Args:
            device (str, optional): Pytorch computation device. Defaults to 'cpu'.
        """
        super(CorrectionNet, self).__init__()
        self.device = device

    def initialize_network(self, object_meta: ObjectMeta, image_meta: ImageMeta) -> None:
        """Initalizes the correction network using the object/image metadata

        Args:
            object_meta (ObjectMeta): Object metadata.
            image_meta (ImageMeta): Image metadata.
        """
        self.object_meta = object_meta
        self.image_meta = image_meta

    @abc.abstractmethod
    def forward(self, x: torch.tensor):
        """Abstract method; must be implemented in subclasses to apply a correction to an object/image and return it
        """
        ...