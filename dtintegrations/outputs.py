from datetime import datetime


class OutputBase(object):
    """
    Represents common features for all returnable objects.

    """

    def __init__(self, raw: dict) -> None:
        """
        Constructs the OutputBase object by setting raw attribute.

        Parameters
        ----------
        raw : dict
            Unmodified dictionary of data received from the REST API.

        """

        # Set attribute from input argument.
        self._raw = raw

    def __repr__(self) -> str:
        return '{}.{}({})'.format(
            self.__class__.__module__,
            self.__class__.__name__,
            self._raw,
        )

    def __str__(self) -> str:
        out = self.__str__recursive([], self, level=0)
        return '\n'.join(out)

    def __str__recursive(self, out: list, obj: object, level: int) -> list:
        # Set the indent level for formatting.
        n_spaces = 4
        l0 = level*' '*n_spaces
        l1 = (level+1)*' '*n_spaces
        l2 = (level+2)*' '*n_spaces

        # At first recursive depth, print object name.
        if level == 0:
            out.append(l0 + str(obj.__class__.__name__) + '(')

        # Append the various public attributes recursively.
        for a in vars(obj):
            # Skip private attributes.
            if a.startswith('_'):
                continue

            # Fetch and evaluate the attribute value / type.
            val = getattr(obj, a)

            # Class objects should be dumped recursively, except for
            # those that are an instance of datetime, like pandas timestamps.
            if hasattr(val, '__dict__') and not isinstance(val, datetime):
                # Other classes should print name with content recursively.
                out.append('{}{}: {} = {}'.format(
                    l1, a, type(val).__name__,
                    str(val.__class__.__name__) + '('))
                self.__str__recursive(out, val, level=level+1)

            # Lists content should be iterated through.
            elif isinstance(val, list):
                out.append('{}{}: {} = {}'.format(
                    l1, a, type(val).__name__, '['))
                self.__str__list(out, val, level+1, l2)
                out.append(l1 + '],')

            # Other types can be printed directly.
            else:
                out.append('{}{}: {} = {},'.format(
                    l1, a, type(val).__name__, str(val)
                ))

        # At the end of each recursive depth, end object paranthesis.
        out.append(l0 + '),')

        return out

    def __str__list(self,
                    out: list,
                    lst: list,
                    level: int,
                    l1: str,
                    ) -> list:
        for val in lst:
            # Class objects should be dumped recursively.
            if hasattr(val, '__dict__'):
                out.append('{}{}'.format(
                    l1, str(val.__class__.__name__) + '('
                ))
                self.__str__recursive(out, val, level=level+2)

            # Everything else can be printed directly.
            else:
                out.append('{}{} = {},'.format(
                    l1, type(val).__name__, str(val)
                ))
        return out
